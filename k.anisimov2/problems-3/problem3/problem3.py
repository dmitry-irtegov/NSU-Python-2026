import math


class Vector:
    def __init__(self, coordinates):
        coordinates = tuple(coordinates)

        if len(coordinates) == 0:
            raise ValueError("vector must contain at least one coordinate")

        for x in coordinates:
            if not isinstance(x, (int, float)):
                raise TypeError("all coordinates must be numbers")

        self.coordinates = coordinates

    def _check_dimension(self, other):
        if not isinstance(other, Vector):
            raise TypeError("operation is supported only for vectors")
        if len(self.coordinates) != len(other.coordinates):
            raise ValueError("vectors must have the same dimension")

    def __add__(self, other):
        self._check_dimension(other)
        return Vector([
            self.coordinates[i] + other.coordinates[i]
            for i in range(len(self.coordinates))
        ])

    def __sub__(self, other):
        self._check_dimension(other)
        return Vector([
            self.coordinates[i] - other.coordinates[i]
            for i in range(len(self.coordinates))
        ])

    def __mul__(self, value):
        if isinstance(value, Vector):
            return self.dot(value)

        if not isinstance(value, (int, float)):
            raise TypeError("vector can be multiplied only by a number or another vector")

        return Vector([
            x * value
            for x in self.coordinates
        ])

    def __rmul__(self, value):
        return self * value

    def __eq__(self, other):
        if not isinstance(other, Vector):
            return False
        return self.coordinates == other.coordinates

    def __getitem__(self, index):
        return self.coordinates[index]

    def __len__(self):
        return len(self.coordinates)

    def __str__(self):
        return "(" + ", ".join(str(x) for x in self.coordinates) + ")"

    def __repr__(self):
        return f"Vector({list(self.coordinates)})"

    def dot(self, other):
        self._check_dimension(other)
        return sum(
            self.coordinates[i] * other.coordinates[i]
            for i in range(len(self.coordinates))
        )

    def length(self):
        return math.sqrt(sum(x * x for x in self.coordinates))

    def dimension(self):
        return len(self.coordinates)