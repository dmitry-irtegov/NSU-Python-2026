import math
import unittest
from typing import Sequence, Self


class Vector:
    def __init__(self, coordinates: Sequence[float]) -> None:
        self._coordinates: tuple[float, ...] = tuple(coordinates)

    def __add__(self, other: Self) -> Self:
        return Vector([a + b for a, b in zip(self._coordinates, other._coordinates)])

    def __sub__(self, other: Self) -> Self:
        return Vector([a - b for a, b in zip(self._coordinates, other._coordinates)])

    def __mul__(self, scalar: float) -> Self:
        return Vector([x * scalar for x in self._coordinates])

    def __rmul__(self, scalar: float) -> Self:
        return self.__mul__(scalar)

    def dot(self, other: Self) -> float:
        return sum([a * b for a, b in zip(self._coordinates, other._coordinates)])

    def length(self) -> float:
        return math.sqrt(self.dot(self))

    def __getitem__(self, index: int) -> float:
        return self._coordinates[index]

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Vector):
            return False
        return self._coordinates == other._coordinates

    def __str__(self) -> str:
        return f"Vector({', '.join(str(x) for x in self._coordinates)})"

    def __len__(self) -> int:
        return len(self._coordinates)


class TestVector(unittest.TestCase):
    def test_add(self) -> None:
        self.assertEqual(
            Vector([1, 2, 3]) + Vector([4, 5, 6]),
            Vector([5, 7, 9])
        )

    def test_subtract(self) -> None:
        self.assertEqual(
            Vector([5, 7, 9]) - Vector([1, 2, 3]),
            Vector([4, 5, 6])
        )

    def test_multiply_by_scalar(self) -> None:
        self.assertEqual(
            Vector([1, 2, 3]) * 2,
            Vector([2, 4, 6])
        )

    def test_right_multiply_by_scalar(self) -> None:
        self.assertEqual(
            3 * Vector([1, 2]),
            Vector([3, 6])
        )

    def test_dot_product(self) -> None:
        self.assertEqual(
            Vector([1, 2, 3]).dot(Vector([4, 5, 6])),
            32.0
        )

    def test_length(self) -> None:
        self.assertAlmostEqual(
            Vector([3, 4]).length(),
            5.0
        )

    def test_getitem(self) -> None:
        v = Vector([10, 20, 30])
        self.assertEqual(v[0], 10)
        self.assertEqual(v[2], 30)

    def test_equal(self) -> None:
        self.assertEqual(Vector([1, 2, 3]), Vector([1, 2, 3]))

    def test_not_equal(self) -> None:
        self.assertNotEqual(Vector([1, 2, 3]), Vector([1, 2, 4]))

    def test_string_representation(self) -> None:
        self.assertEqual(str(Vector([1, 2, 3])), "Vector(1, 2, 3)")

    def test_len(self) -> None:
        self.assertEqual(len(Vector([1, 2, 3, 4])), 4)

    def test_zero_vector_length(self) -> None:
        self.assertEqual(Vector([0, 0, 0]).length(), 0.0)

    def test_add_large_vectors(self) -> None:
        v1 = Vector(list(range(100)))
        v2 = Vector(list(range(100, 200)))
        expected = Vector([i + (i + 100) for i in range(100)])
        self.assertEqual(v1 + v2, expected)

    def test_subtract_large_vectors(self) -> None:
        v1 = Vector(list(range(200, 300)))
        v2 = Vector(list(range(100)))
        expected = Vector([200 for _ in range(100)])
        self.assertEqual(v1 - v2, expected)

    def test_scalar_multiply_large_vector(self) -> None:
        v = Vector(list(range(100)))
        expected = Vector([i * 3 for i in range(100)])
        self.assertEqual(v * 3, expected)

    def test_dot_product_large_vectors(self) -> None:
        v1 = Vector([1 for _ in range(100)])
        v2 = Vector([2 for _ in range(100)])
        self.assertEqual(v1.dot(v2), 200.0)

    def test_large_vector_length(self) -> None:
        v = Vector([1 for _ in range(100)])
        self.assertAlmostEqual(v.length(), math.sqrt(100))


if __name__ == "__main__":
    unittest.main()