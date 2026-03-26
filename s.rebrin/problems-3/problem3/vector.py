from typing import List, Union
from math import sqrt


class Vector:
    def __init__(self, arr: List[int]):
        self.arr = arr
        self.n = len(arr)

    def __add__(self, other: Union["Vector", int]) -> "Vector":
        if isinstance(other, Vector):
            if self.n != other.n:
                raise ValueError("Vectors must be the same size")
            return Vector([a + b for a, b in zip(self.arr, other.arr)])
        elif isinstance(other, int):
            return Vector([a + other for a in self.arr])
        else:
            return NotImplemented

    def __sub__(self, other: Union["Vector", int]) -> "Vector":
        if isinstance(other, Vector):
            if self.n != other.n:
                raise ValueError("Vectors must be the same size")
            return Vector([a - b for a, b in zip(self.arr, other.arr)])
        elif isinstance(other, int):
            return Vector([a - other for a in self.arr])
        else:
            return NotImplemented

    def dot(self, other: "Vector") -> int:
        if self.n != other.n:
            raise ValueError("Vectors must be the same size")
        return sum(a * b for a, b in zip(self.arr, other.arr))

    def vector_len(self) -> float:
        return sqrt(sum(a * a for a in self.arr))

    def __getitem__(self, i: int) -> int:
        return self.arr[i]

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Vector):
            return False
        return self.arr == other.arr

    def __repr__(self) -> str:
        return f"Vector({self.arr})"
