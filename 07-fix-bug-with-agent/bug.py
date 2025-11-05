# Deliberately buggy code for Lab 07

def calculate_average(numbers):
    total = 0
    for n in numbers:
        total += n

    # BUG: len(total) - incorrect, total is an integer
    return total / len(total)


values = [10, 20, 30, 40]
result = calculate_average(values)
print("Average is:", result)