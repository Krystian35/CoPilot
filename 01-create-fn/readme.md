# Lab 01 — Generate a function from a comment (Python)

### 🎯 Goal
Generate Python functions **only from comments**, without writing code manually.

---

## ✅ Task

1. Create a new Python file (e.g., `main.py`).
2. Add comment(s) describing the function(s).
3. Press Enter → accept Copilot’s suggestion with **Tab**.
4. Run the script to verify the output.

> Do not write code. Only comments.

---

## ✏️ Example comments (Copilot will generate the functions)

```python
# Create a function "average" that receives a list of numbers and returns the average value.
```

```python
# Create a function that takes a list of words and returns only the words longer than 5 characters.
```

```python
# Create a function "celsius_to_fahrenheit" that receives a temperature in Celsius and returns it converted to Fahrenheit.
```

```python
# Create a function "max_positive_value" that receives a list of numbers and returns the highest value. Ignore negative numbers.
```

Test the output

After Copilot generates the functions, add something like:

```python
print(average([2, 4, 6, 8]))
print(filter_long_words(["cat", "weather", "code", "automation"]))
print(celsius_to_fahrenheit(25))
print(max_positive_value([3, -1, 8, -5, 2]))
```

## Success criteria

- Functions were generated from comments using Copilot.
- You did not write any code manually.
- Script runs and prints expected results.
- You understand what the generated code does.