# Lab 08 — Convert PowerShell to Bash using Copilot

### 🎯 Goal
Use **Copilot Chat (Agent Mode)** to convert an existing PowerShell script into an equivalent Bash script.

---

## ✅ Task

1. Open the PowerShell file `cleanup.ps1` in this folder.
2. Use Copilot Chat to:
   - explain what the script does,
   - rewrite it in Bash,
   - save output to `cleanup.sh`.

> You should **not rewrite the script manually** — let Copilot do the conversion.

---

## 🔧 Prompts to use

### 1. Understand the script
```
/explain Explain what this PowerShell script does.
```

### 2. Convert to Bash
```
Convert this PowerShell script to Bash with the same behavior.
Use find, xargs and standard Bash syntax.
```

### 3. Optional — make it executable
```
Modify the script to accept arguments: --path and --days
```

---

## ✅ Success criteria

- `cleanup.sh` exists and contains a Bash implementation
- Behavior matches PowerShell version
- No manual rewriting — conversion done by Copilot

---