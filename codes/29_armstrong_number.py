def is_armstrong(number):
    if number < 0:
        return False

    digits = [int(digit) for digit in str(number)]
    power = len(digits)
    total = 0
    for digit in digits:
        total += digit ** power

    return total == number
