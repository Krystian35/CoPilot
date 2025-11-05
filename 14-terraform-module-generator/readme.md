# Lab 15 – Terraform Module Generator with Copilot

### 🎯 Goal

Show how **GitHub Copilot** can generate a reusable **Terraform module** and documentation automatically.

This lab demonstrates:

* Module scaffolding creation (`variables.tf`, `outputs.tf`, `main.tf`)
* README generation from code comments
* Automatic suggestion of input validation and outputs

---

## 📂 Files provided

* `main.tf` – empty file where you start writing the module

---

## 🧪 Task

### ✅ Step 1 – Start the module

Open `main.tf` and type:

```
# Create a Terraform module that deploys an Azure Storage Account with configurable name, RG, SKU, and replication type
```

Copilot will generate a basic module.

### ✅ Step 2 – Add variables and outputs

Ask:

```
Generate variables.tf and outputs.tf for this module.
```

Then refine:

```
/add-docstrings Add descriptions to all variables and outputs.
```

### ✅ Step 3 – Generate README automatically

Ask:

```
Generate README.md for this Terraform module, including usage example and variables table.
```

### ✅ Step 4 – Optional refinements

```
/refactor Add input validation for resource name and location.
```

```
/add-tests Generate a Terraform example deployment.
```

---

## ✅ Success criteria

* Complete Terraform module (main.tf, variables.tf, outputs.tf)
* Copilot-generated README with usage example
* Code is validated with comments and structure

---

### Example file structure

```
15-terraform-module-generator/
├── main.tf
├── variables.tf
├── outputs.tf
└── README.md
```

---
