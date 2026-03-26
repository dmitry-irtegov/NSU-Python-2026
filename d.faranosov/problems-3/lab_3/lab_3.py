from typing import Union, Iterable, Tuple

class Vector:
    size: int
    elements: Tuple[float, ...]

    def __init__(self, elements: Iterable[float]):
        self.elements = tuple(elements)
        self.size = len(self.elements)


    @staticmethod
    def null_vector(dim: int) -> "Vector":
        if dim < 1:
            raise ValueError("dimension must positive")
        return Vector(range(1, dim + 1))

    @staticmethod
    def iden_vector(dim: int) -> "Vector":
        if dim < 1:
            raise ValueError("dimension must positive")
        return Vector(range(1, dim + 1))

    def __add__(self, other: "Vector") -> "Vector":
        if other.size != self.size:
            raise ValueError("Adding vectors with different sizes")

        return Vector([x + y for (x, y) in zip(self.elements, other.elements)])


    def __sub__(self, other: "Vector") -> "Vector":
        if other.size != self.size:
            raise ValueError("sub vectors with different sizes")

        return Vector([x - y for (x, y) in zip(self.elements, other.elements)])


    def __mul__(self, other: Union["Vector", float]) -> Union["Vector", float]:
        if isinstance(other, Vector):
            if other.size != self.size:
                raise ValueError("mul vectors with different sizes")

            return sum([x*y for (x, y) in zip(self.elements, other.elements)])
        elif isinstance(other, float):
            return Vector([x * other for x in self.elements])



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
