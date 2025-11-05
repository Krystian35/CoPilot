# Lab 05 — Convert CSV to JSON using Copilot

### 🎯 Goal

Use **Copilot Chat (Agent Mode)** to generate Python code that reads a CSV file and outputs a JSON file.

---

## ✅ Task

1. In this folder, you have `data.csv`.
2. Ask Copilot to create file `data.json` which contains the data

> You should not code manually — describe what you want in natural language and let Copilot convert data.

---

## 🔧 Prompts to use

### Generate script

```
Convert this file into `data.json`
```

### Optional — pretty formatting

```
Create additional file `data.yaml`
```


---

## ✅ Success criteria

* Script reads CSV and saves JSON.

---

## 📄 Example CSV (`data.csv`)

```
id,name,role
1,Alice,Admin
2,Bob,Developer
3,Eve,Security
```

---

### Expected `output.json`

```json
[
  { "id": "1", "name": "Alice", "role": "Admin" },
  { "id": "2", "name": "Bob", "role": "Developer" },
  { "id": "3", "name": "Eve", "role": "Security" }
]
```

---
