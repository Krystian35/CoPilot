# Documentation: average function

## Function Overview

The `average` function calculates the arithmetic mean of a list or iterable of numeric values. It is defined in `example01.py`.

## Function Definition

```python
def average(numbers):
    """
    Calculate the arithmetic mean of a list of numbers.

    Args:
        numbers (iterable): A list or iterable of numeric values.

    Returns:
        float: The average value of the input numbers.

    Raises:
        ZeroDivisionError: If the input list is empty.
    """
    total = 0  # Initialize total sum to zero
    count = 0  # Initialize count of numbers to zero

    for number in numbers:
        total += number  # Add each number to the total sum
        count += 1       # Increment count for each number processed

    return total / count  # Return the average (total divided by count)
```

## Example Usage

```python
result = average([10, 20, 30, 40])  # Call the function with a sample list
print(result)  # Print the result to the console
```

## Notes

- The function will raise a `ZeroDivisionError` if the input list is empty.
- Inline comments are included for clarity.
