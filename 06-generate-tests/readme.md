# Lab 07 — Generate Unit Tests Using Copilot

### 🎯 Goal

Use **Copilot Chat (Agent Mode)** to automatically generate unit tests (`pytest`) for existing functions.

---

## ✅ Task

1. Open the file `function.py` in this folder.
2. Use Copilot Chat to:

   * analyze the functions,
   * generate a `test_function.py` file with unit tests.
3. Run the tests.

> You should not manually write test code — let Copilot generate it.

---

## 🔧 Prompts to use

### 1. Understand what needs to be tested

```
/explain What functions exist in this file and what are their expected behaviors?
```

### 2. Generate unit tests

```
Generate pytest unit tests for all functions in this file. Create a new file named test_function.py.
```

### 3. Optional — edge cases

```
Add edge case tests (null/empty input, negative values).
```

---

## ✅ Success criteria

* Copilot created `test_function.py`.
* Tests cover all functions from `function.py`.
* Tests run without errors.

---
