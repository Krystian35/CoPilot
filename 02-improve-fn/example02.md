# Documentation: filter_long_words function

## Function Overview

The `filter_long_words` function returns a list of words from the input that are longer than 5 characters. It is defined in `example02.py`.

## Function Definition

```python
def filter_long_words(words):
    """
    Return a list of words from the input that are longer than 5 characters.

    Args:
        words (list): List of strings to filter.

    Returns:
        list: List containing words with length greater than 5.
    """
    result = []  # Initialize an empty list to store long words

    for word in words:
        if len(word) > 5:  # Check if the word length is greater than 5
            result.append(word)  # Add the word to the result list

    return result  # Return the filtered list
```

## Example Usage

```python
print(filter_long_words(["apple", "code", "automation", "AI", "python"]))  # Example usage
```

**Output:**

```
['automation', 'python']
```

## Notes

- Only words with more than 5 characters are included in the result.
- Inline comments are included for clarity.
