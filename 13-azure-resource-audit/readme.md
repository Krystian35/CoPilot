# Lab 14 – Azure Resource Audit with GitHub Copilot

### 🎯 Goal

Use **GitHub Copilot** to generate and improve an **Azure resource audit script**. The goal is to show how Copilot can assist IT admins in:

1. Generating PowerShell or Azure CLI commands to list and audit resources
2. Adding export options (CSV / JSON)
3. Improving code readability and adding comments automatically

---

## 📂 Files provided

* `azure_audit.ps1` – base script template for auditing Azure resources

---

## 🧪 Task

### ✅ Step 1 – Ask Copilot to create an audit script

In the empty file `azure_audit.ps1`, start typing:

```
# Write a PowerShell script to list all Resource Groups with their locations and tags in Azure
```

Copilot should suggest a full script using `az group list` or `Get-AzResourceGroup`.

### ✅ Step 2 – Add more audit checks

Prompt Copilot:

```
Add sections that list all VMs, Storage Accounts, and App Services with their resource group, location, and SKU.
```

### ✅ Step 3 – Export results

Ask Copilot:

```
Add logic to export all results to CSV and JSON.
```

### ✅ Step 4 – Add comments and refactor

Prompt:

```
/add-docstrings Add inline comments explaining each part of the script.
/refactor Improve structure and readability.
```

---

## ✅ Success criteria

* Script lists multiple Azure resource types
* Includes export to CSV/JSON
* Copilot added documentation/comments

---

## 🚀 Optional

```
/extend Add audit for Defender for Cloud recommendations.
```

```
/refactor Use Az PowerShell module instead of Azure CLI.
```

---

### Example file structure

```
14-azure-resource-audit/
├── azure_audit.ps1
└── README.md
```

---

