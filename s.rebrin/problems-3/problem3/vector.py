from math import sqrt
from typing import Iterable, Tuple, Union


Number = Union[int, float]


class Vector:
    arr: Tuple[float, ...]

    def __init__(self, arr: Iterable[Number]):
        converted = []
        for x in arr:
            if not isinstance(x, (int, float)):
                raise ValueError("Must be int or float")
            converted.append(float(x))

        self.arr = tuple(converted)

    def __len__(self) -> int:
        return len(self.arr)

    def __add__(self, other: object) -> "Vector":
        if isinstance(other, Vector):
            if len(self) != len(other):
                raise ValueError("Vectors must be the same size")
            return Vector(tuple(a + b for a, b in zip(self.arr, other.arr)))
        elif isinstance(other, (int, float)):
            return Vector(tuple(a + other for a in self.arr))
        return NotImplemented

    def __radd__(self, other: Number) -> "Vector":
        return self + other

    def __sub__(self, other: object) -> "Vector":
        if isinstance(other, Vector):
            if len(self) != len(other):
                raise ValueError("Vectors must be the same size")
            return Vector(tuple(a - b for a, b in zip(self.arr, other.arr)))
        elif isinstance(other, (int, float)):
            return Vector(tuple(a - other for a in self.arr))
        return NotImplemented

    def __rsub__(self, other: Number) -> "Vector":
        if isinstance(other, (int, float)):
            return Vector(tuple(other - a for a in self.arr))
        return NotImplemented

    def __mul__(self, other: Number) -> "Vector":
        return Vector(tuple(a * other for a in self.arr))

    def __rmul__(self, other: Number) -> "Vector":
        return self * other

    def dot(self, other: "Vector") -> float:
        if len(self) != len(other):
            raise ValueError("Vectors must be same size")
        return sum(a * b for a, b in zip(self.arr, other.arr))

    def length(self) -> float:
        return sqrt(sum(a * a for a in self.arr))

    def __getitem__(self, i: int) -> float:
        return self.arr[i]

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Vector):
            return NotImplemented
        return self.arr == other.arr

    def __repr__(self) -> str:
        return f"Vector({self.arr})"
