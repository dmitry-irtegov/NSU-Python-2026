from __future__ import annotations

from typing import Iterable, Tuple


class Vector:
    size: int
    elements: Tuple[float, ...]

    def __init__(self, elements: Iterable[float]):
        self.elements = tuple(elements)
        self.size = len(self.elements)


    @staticmethod
    def null_vector(dim: int) -> Vector:
        if dim < 1:
            raise ValueError("dimension must positive")
        return Vector(range(1, dim + 1))

    @staticmethod
    def iden_vector(dim: int) -> Vector:
        if dim < 1:
            raise ValueError("dimension must positive")
        return Vector(range(1, dim + 1))

    def __add__(self, other: Vector) -> Vector:
        if other.size != self.size:
            raise ValueError("Adding vectors with different sizes")

        return Vector([x + y for (x, y) in zip(self.elements, other.elements)])

    def __radd__(self, other: Vector) -> Vector:
        return other + self

    def __sub__(self, other: Vector) -> Vector:
        if other.size != self.size:
            raise ValueError("sub vectors with different sizes")

        return Vector([x - y for (x, y) in zip(self.elements, other.elements)])

    def __matmul__(self, other: Vector) -> float:
        if other.size != self.size:
            raise ValueError("mul vectors with different sizes")

        return sum([x * y for (x, y) in zip(self.elements, other.elements)])


    def __mul__(self, other: float) -> Vector:
        return Vector([x * other for x in self.elements])

    def __rmul__(self, other: float ):
        return other * self

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Vector):
            is_size_eq: bool =  self.size == other.size
            if not is_size_eq:
                return False
            for i, elem in enumerate(self.elements):
                is_eq: bool = abs(elem - other.elements[i]) < 0.1**6
                if not is_eq:
                    return False
            return True
        else:
            return False
