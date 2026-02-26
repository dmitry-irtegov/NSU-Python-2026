from __future__ import annotations

from typing import List, Union


class Vector:
    size: int
    elements: List[float]

    def __init__(self, elements: List[float]):
        if len(elements) == 0:
            raise ValueError("dimension must positive")
        self.size = len(elements)
        self.elements = elements

    @staticmethod
    def null_vector(dim: int) -> Vector:
        if dim < 1:
            raise ValueError("dimension must positive")
        return Vector([0 for _ in range(1, dim + 1)])

    @staticmethod
    def iden_vector(dim: int) -> Vector:
        if dim < 1:
            raise ValueError("dimension must positive")
        return Vector([1 for _ in range(1, dim + 1)])

    def __add__(self, other: Vector) -> Vector:
        if isinstance(other, Vector):
            if other.size != self.size:
                raise ValueError("Adding vectors with different sizes")

            return Vector([x + y for (x, y) in zip(self.elements, other.elements)])
        else:
            raise TypeError("Adding with not a vector")

    def __sub__(self, other: Vector) -> Vector:
        if isinstance(other, Vector):
            if other.size != self.size:
                raise ValueError("sub vectors with different sizes")

            return Vector([x - y for (x, y) in zip(self.elements, other.elements)])
        else:
            raise TypeError("sub with not a vector")

    def __mul__(self, other: Union[Vector, float]) -> Union[Vector, float]:
        if isinstance(other, Vector):
            if other.size != self.size:
                raise ValueError("mul vectors with different sizes")

            return sum([x*y for (x, y) in zip(self.elements, other.elements)])
        elif isinstance(other, float):
            return Vector([x * other for x in self.elements])
        else:
            raise TypeError("multiply with smth not a Vector or float")

    def __eq__(self, other) -> bool:
        if isinstance(other, Vector):
            is_size_eq =  self.size == other.size
            if not is_size_eq:
                return False
            for i, elem in enumerate(self.elements):
                is_eq = abs(elem - other.elements[i]) < 0.1**6
                if not is_eq:
                    return False
            return True
        else:
            return False
