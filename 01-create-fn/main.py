# Create a function "average" that receives a list of numbers and returns the average value.
def average(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)


# Create a function that takes a list of words and returns only the words longer than 5 characters.
def filter_long_words(words):
    return [word for word in words if len(word) > 5]


# Create a function "celsius_to_fahrenheit" that receives a temperature in Celsius and returns it converted to Fahrenheit.
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Create a function "max_positive_value" that receives a list of numbers and returns the highest value. Ignore negative numbers.
def max_positive_value(numbers):
    max_value = None
    for n in numbers:
        if n > 0:
            if max_value is None or n > max_value:
                max_value = n
    return max_value


if __name__ == "__main__":
    # Collect outputs in the original logical order and print them at the end of the file.
    print(average([10, 20, 30]))  # originally a module-level print
    print(average([1, 2, 3, 4, 5]))  # original __main__ prints
    print(average([]))

    print(filter_long_words(["hello", "world", "python", "programming", "code"]))

    print(celsius_to_fahrenheit(0))    # Output: 32.0
    # Print average temperature in Poland in Fahrenheit
    print(celsius_to_fahrenheit(10))   # Output: 50.0

    maxv = max_positive_value([-10, -5, 0, 3, 7, 2])
    # Original code printed a status message inside the function and then printed the return value.
    # We reproduce both outputs here but keep prints at the end.
    print("Max positive value found:", maxv)
    print(maxv)

