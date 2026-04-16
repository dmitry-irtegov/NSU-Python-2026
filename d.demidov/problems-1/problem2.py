import uuid


def clamp_array_to_bounds(
        nums: list[int | float],
        lower_bound: int | float,
        upper_bound: int | float
) -> list[int | float]:
    return [max(lower_bound, min(num, upper_bound)) for num in nums]


def test_clamp_array_to_bounds() -> None:
    random_numbers = [uuid.uuid4().int for _ in range(10)]
    lower_bound = uuid.uuid4().int
    upper_bound = uuid.uuid4().int

    lower_bound, upper_bound = min(lower_bound, upper_bound), max(lower_bound, upper_bound)

    res = clamp_array_to_bounds(random_numbers, lower_bound, upper_bound)

    print(lower_bound, upper_bound)
    print(random_numbers)
    print(res)

    assert all(lower_bound <= num <= upper_bound for num in res)


if __name__ == "__main__":
    test_clamp_array_to_bounds()
