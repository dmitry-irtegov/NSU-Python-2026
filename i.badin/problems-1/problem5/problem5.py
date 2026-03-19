def factorize(number: int) -> list[list[int]]:
    if number < 1:
        raise ValueError("number must be a positive integer")

    factors: list[list[int]] = []
    divisor = 2

    while divisor * divisor <= number:
        power = 0
        while number % divisor == 0:
            number //= divisor
            power += 1

        if power > 0:
            factors.append([divisor, power])

        divisor = 3 if divisor == 2 else divisor + 2

    if number > 1:
        factors.append([number, 1])

    return factors
