def decimal_to_binary(number):
    if number < 0:
        raise ValueError("Negative numbers are not allowed")
    if number == 0:
        return "0"

    bits = []
    current = number

    while current > 0:
        current, remainder = divmod(current, 2)
        bits.append(str(remainder))

    return "".join(reversed(bits))
