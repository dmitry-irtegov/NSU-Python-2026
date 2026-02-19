def clip_numbers(numbers: list[float], a: float, b: float) -> list[float]:
    if a > b:
        raise ValueError("Lower bound 'a' must be less than or equal to upper bound 'b'.")
    return [max(a, min(number, b)) for number in numbers]
