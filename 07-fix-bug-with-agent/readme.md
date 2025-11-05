# Lab 07 – Fix bug using Copilot Agent

## 🎯 Goal

Use **GitHub Copilot Agent mode** to identify and fix a bug in an existing Python script.

---

## ✅ What you will learn

* How to use **Copilot Chat + Agent mode** to understand unfamiliar code
* How to fix errors using `/fix` and step-by-step guidance
* How to validate the fix by running the program

---

## 📂 Files in this folder

* `bug.py` – contains the buggy Python code you will fix

---

## 🧪 Task

Open the file `bug.py` in VS Code.

Your goal is to:

1. Ask Copilot **what this code does**
2. Ask Copilot to **find and fix the bug** using Agent Mode
3. Validate that the bug is fixed by running the program

---

## 🔧 Instructions

### 1. Understand the code

Open `bug.py`, select the code and use prompt:

```
/explain What does this code do? Explain step by step.
```

### 2. Enable Copilot Agent

In Copilot Chat → mode dropdown → select **Agent**

Then execute:

```
/fix This code throws an error when executed. Find the root cause and fix it.
```

### 3. Verify

Run the app:

```
python bug.py
```

If it works correctly → ✅ lab completed

---

## ✅ Success criteria

You have successfully completed this lab when:

* Copilot Agent finds the error
* The code executes without crashing
* You understand **what was broken and how Agent fixed it**

---

## 🚀 Optional

Ask Copilot:

```
/add-comments Add comments to make this code easier to understand.
```

> Tip: The goal is to **let Copilot work for you** — don’t fix the bug manually.

---

Done? Move to the next lab → `08-genera
