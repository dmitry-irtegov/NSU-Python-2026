from math import sqrt
from typing import Iterable


class Vector:
    arr: float

    def __init__(self, arr: Iterable[float]):
        self.arr = tuple(float(x) for x in arr)

    def __len__(self) -> int:
        return len(self.arr)

    def __add__(self, other: object) -> "Vector":
        if isinstance(other, Vector):
            if len(self) != len(other):
                raise ValueError("Vectors must be the same size")
            return Vector(a + b for a, b in zip(self.arr, other.arr))
        elif isinstance(other, (int, float)):
            return Vector(a + other for a in self.arr)
        return NotImplemented

    def __radd__(self, other: int) -> "Vector":
        if isinstance(other, (int, float)):
            return self + other
        return NotImplemented

    def __sub__(self, other: object) -> "Vector":
        if isinstance(other, Vector):
            if len(self) != len(other):
                raise ValueError("Vectors must be the same size")
            return Vector(a - b for a, b in zip(self.arr, other.arr))
        elif isinstance(other, int):
            return Vector(a - other for a in self.arr)
        return NotImplemented

    def __rsub__(self, other: int) -> "Vector":
        if isinstance(other, int):
            return Vector(other - a for a in self.arr)
        return NotImplemented

    def __mul__(self, other: int) -> "Vector":
        if isinstance(other, int):
            return Vector(a * other for a in self.arr)
        return NotImplemented

    def __rmul__(self, other: int) -> "Vector":
        if isinstance(other, int):
            return self * other
        return NotImplemented

    def dot(self, other: "Vector") -> int:
        if not isinstance(other, Vector):
            raise TypeError("Expected Vector")
        if len(self) != len(other):
            raise ValueError("Vectors must be the same size")
        return sum(a * b for a, b in zip(self.arr, other.arr))

    def length(self) -> float:
        return sqrt(sum(a * a for a in self.arr))

    def __getitem__(self, i: int) -> float:
        if not isinstance(i, int):
            raise TypeError("Index must be int")
        return self.arr[i]

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Vector):
            return NotImplemented
        return self.arr == other.arr

    def __repr__(self) -> str:
        return f"Vector({self.arr})"
