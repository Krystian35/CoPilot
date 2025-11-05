# Deliberately buggy code for Lab 07

def calculate_average(numbers):
    # handle empty input explicitly
    if not numbers:
        raise ValueError("numbers must not be empty")

    # use built-in sum and correct length
    total = sum(numbers)
    return total / len(numbers)


values = [10, 20, 30, 40]
result = calculate_average(values)
print("Average is:", result)