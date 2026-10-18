def find_max_min(numbers):
    if not numbers:
        raise ValueError("List cannot be empty")

    maximum = numbers[0]
    minimum = numbers[0]

    for value in numbers[1:]:
        if value > maximum:
            maximum = value
        if value < minimum:
            minimum = value

    return maximum, minimum
