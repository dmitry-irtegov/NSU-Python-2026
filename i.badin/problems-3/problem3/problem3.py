from collections.abc import Iterable
import math
from typing import Self


class Vector:
    def __init__(self, coordinates: Iterable[float]) -> None:
        self._coordinates: tuple[float, ...] = tuple(coordinates)

    def __add__(self, other: Self) -> Self:
        return type(self)(a + b for a, b in zip(self._coordinates, other._coordinates))

    def __sub__(self, other: Self) -> Self:
        return type(self)(a - b for a, b in zip(self._coordinates, other._coordinates))

    def __mul__(self, scalar: float) -> Self:
        return type(self)(coordinate * scalar for coordinate in self._coordinates)

    def __rmul__(self, scalar: float) -> Self:
        return self * scalar

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Vector):
            return False

        return self._coordinates == other._coordinates

    def __getitem__(self, index: int) -> float:
        return self._coordinates[index]

    def __len__(self) -> int:
        return len(self._coordinates)

    def __str__(self) -> str:
        return f"Vector({', '.join(str(coordinate) for coordinate in self._coordinates)})"

    def dot(self, other: Self) -> float:
        return sum(a * b for a, b in zip(self._coordinates, other._coordinates))

    def length(self) -> float:
        return math.sqrt(self.dot(self))
