from collections.abc import Iterable, Iterator
from typing import Any, Protocol


class OrderedValue(Protocol):
    def __lt__(self, other: Any, /) -> bool: ...

    def __le__(self, other: Any, /) -> bool: ...

    def __gt__(self, other: Any, /) -> bool: ...

    def __ge__(self, other: Any, /) -> bool: ...


def clip_values[ValueT: OrderedValue](
    values: Iterable[ValueT],
    lower: ValueT,
    upper: ValueT,
) -> Iterator[ValueT]:
    if upper < lower:
        message: str = f"upper boundary {upper} is less than lower boundary {lower}"
        raise ValueError(message)

    return (min(max(value, lower), upper) for value in values)
