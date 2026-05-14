from collections.abc import Iterable, Iterator

OrderedNumber = int | float


def clip_numbers(
    numbers: Iterable[OrderedNumber],
    lower: OrderedNumber,
    upper: OrderedNumber,
) -> Iterator[OrderedNumber]:
    if upper < lower:
        message: str = f"upper boundary {upper} is less than lower boundary {lower}"
        raise ValueError(message)

    return (min(max(number, lower), upper) for number in numbers)
