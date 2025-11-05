def average(numbers):
    total = 0
    count = 0

    for number in numbers:
        total += number
        count += 1

    return total / count


result = average([10, 20, 30, 40])
print(result)
