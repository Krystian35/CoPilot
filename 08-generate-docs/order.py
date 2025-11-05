from dataclasses import dataclass
from typing import List, Dict, Any
from pathlib import Path
import json

# Order domain objects
@dataclass
class Product:
    sku: str
    title: str
    price: float
    stock: int


class ProductCatalog:
    def __init__(self):
        self._items: Dict[str, Product] = {
            "BK-001": Product("BK-001", "Dune", 39.99, 12),
            "BK-002": Product("BK-002", "Neuromancer", 29.99, 8),
            "BK-003": Product("BK-003", "Clean Code", 59.99, 5),
        }

    def get(self, sku: str) -> Product:
        return self._items[sku]

    def has_stock(self, sku: str, qty: int) -> bool:
        p = self.get(sku)
        return p.stock >= qty

    def reserve(self, sku: str, qty: int) -> None:
        p = self.get(sku)
        if p.stock < qty:
            raise ValueError("Insufficient stock")
        p.stock -= qty


class PaymentGateway:
    def charge(self, amount: float, card_token: str) -> str:
        if amount <= 0:
            raise ValueError("Amount must be positive")
        if not card_token or not card_token.startswith("tok_"):
            raise ValueError("Invalid payment token")
        return "ch_" + card_token[4:]


class Notifier:
    def send(self, address: str, subject: str, body: str) -> None:
        print(f"[MAIL] To:{address} | {subject}\n{body}")


# Pipeline flow
class OrderService:
    def __init__(self, catalog: ProductCatalog, payments: PaymentGateway, notifier: Notifier):
        self.catalog = catalog
        self.payments = payments
        self.notifier = notifier
        self.pipeline: List[str] = [
            "validate_request",
            "price_items",
            "reserve_inventory",
            "charge_payment",
            "send_notification",
        ]

    def process(self, order: Dict[str, Any]) -> Dict[str, Any]:
        self._validate_request(order)
        total = self._price_items(order)
        self._reserve_inventory(order)
        charge_id = self._charge_payment(total, order["payment_token"])
        self._send_notification(order, total, charge_id)
        return {"total": total, "charge_id": charge_id}

    # --- Steps in the flow ---
    def _validate_request(self, order: Dict[str, Any]) -> None:
        if "customer_email" not in order:
            raise ValueError("Missing customer email")
        if "items" not in order or not order["items"]:
            raise ValueError("Order must contain at least one item")
        for line in order["items"]:
            if not self.catalog.has_stock(line["sku"], line["qty"]):
                raise ValueError(f"No stock for {line['sku']}")

    def _price_items(self, order: Dict[str, Any]) -> float:
        total = 0.0
        for line in order["items"]:
            product = self.catalog.get(line["sku"])
            total += product.price * line["qty"]
        return round(total, 2)

    def _reserve_inventory(self, order: Dict[str, Any]) -> None:
        for line in order["items"]:
            self.catalog.reserve(line["sku"], line["qty"])

    def _charge_payment(self, amount: float, token: str) -> str:
        return self.payments.charge(amount, token)

    def _send_notification(self, order: Dict[str, Any], total: float, charge_id: str) -> None:
        subject = "Order confirmation"
        body = json.dumps({"total": total, "charge_id": charge_id, "items": order["items"]}, indent=2)
        self.notifier.send(order["customer_email"], subject, body)

