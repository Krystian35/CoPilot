# Order service (order.py)

## Description

This module implements a tiny order processing pipeline for a bookstore/sample store. It provides domain objects and a simple service pipeline that:

- Validates an incoming order
- Prices items using a `ProductCatalog`
- Reserves inventory
- Charges a payment via a `PaymentGateway`
- Sends a notification via a `Notifier`

Main classes:

- `Product` — dataclass describing a product (sku, title, price, stock)
- `ProductCatalog` — in-memory product store with `get`, `has_stock`, and `reserve`
- `PaymentGateway` — simple payment simulator; accepts tokens starting with `tok_` and returns a charge id
- `Notifier` — prints a confirmation message to stdout (simulates email)
- `OrderService` — composes the above and runs the processing pipeline

The code is lightweight and depends only on the Python standard library.

## Usage example

Save this snippet as `example_run.py` next to `order.py` (or run it in an interactive interpreter):

```python
from order import ProductCatalog, PaymentGateway, Notifier, OrderService

catalog = ProductCatalog()
payments = PaymentGateway()
notifier = Notifier()
service = OrderService(catalog, payments, notifier)

order = {
    "customer_email": "alice@example.com",
    "payment_token": "tok_visa_1234",
    "items": [
        {"sku": "BK-001", "qty": 2},
        {"sku": "BK-003", "qty": 1},
    ],
}

result = service.process(order)
print("Result:", result)
```

Expected output (stdout) will include the notifier print and the printed result, for example:

```
[MAIL] To:alice@example.com | Order confirmation
{
  "total": 139.97,
  "charge_id": "ch_visa_1234",
  "items": [
    {"sku": "BK-001", "qty": 2},
    {"sku": "BK-003", "qty": 1}
  ]
}
Result: {'total': 139.97, 'charge_id': 'ch_visa_1234'}
```

Note: the exact `charge_id` string is generated from the provided token (`tok_...` -> `ch_...`).

## Instructions to run (Windows PowerShell)

1. Make sure you have Python 3.8+ installed.
2. Open PowerShell and change into the `08-generate-docs` directory:

```powershell
cd "c:\Users\KrystianPilch\Desktop\CoPilot\CoPilot\08-generate-docs"
```

3. Create the example file (if you didn't already) named `example_run.py` and paste the usage snippet above.
4. Run the example:

```powershell
python example_run.py
```

Since the module has no external dependencies, no requirement files or installs are required.

## Error modes & quick tests

- Missing `customer_email` or empty `items` will raise `ValueError` during validation.
- Ordering more items than available stock raises `ValueError` (handled by `ProductCatalog.has_stock`).
- Invalid payment token (not starting with `tok_`) raises `ValueError` from `PaymentGateway.charge`.

Try these variations to exercise error flows (modify `order` in the example):

- Simulate out-of-stock: set `qty` to a number larger than the product `stock` (see `ProductCatalog` initial stocks in `order.py`).
- Invalid token: set `payment_token` to `"bad_token"`.

## Notes

- The `Notifier.send` prints to stdout — replace with an actual email client in production.
- The `PaymentGateway` is a simple simulator: swap it with a real payments integration for real charges.

---

File: `order.py` (module) — this README documents how to use and run that file.
