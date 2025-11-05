def filter_long_words(words):
    result = []

    for word in words:
        if len(word) > 5:
            result.append(word)

    return result


print(filter_long_words(["apple", "code", "automation", "AI", "python"]))
