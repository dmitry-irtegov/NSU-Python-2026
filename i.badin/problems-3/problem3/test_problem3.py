import math
import unittest

from problem3 import Vector


class VectorTests(unittest.TestCase):
    def test_vector_can_be_created_from_tuple(self) -> None:
        self.assertEqual(Vector((1, 2, 3)), Vector([1, 2, 3]))

    def test_vector_can_be_created_from_lazy_iterator(self) -> None:
        coordinates = (coordinate for coordinate in [1, 2, 3])

        self.assertEqual(Vector(coordinates), Vector([1, 2, 3]))

    def test_add(self) -> None:
        self.assertEqual(
            Vector([1, 2, 3]) + Vector([4, 5, 6]),
            Vector([5, 7, 9]),
        )

    def test_subtract(self) -> None:
        self.assertEqual(
            Vector([5, 7, 9]) - Vector([1, 2, 3]),
            Vector([4, 5, 6]),
        )

    def test_multiply_by_scalar(self) -> None:
        self.assertEqual(
            Vector([1, 2, 3]) * 2,
            Vector([2, 4, 6]),
        )

    def test_right_multiply_by_scalar(self) -> None:
        self.assertEqual(
            3 * Vector([1, 2]),
            Vector([3, 6]),
        )

    def test_dot_product(self) -> None:
        self.assertEqual(
            Vector([1, 2, 3]).dot(Vector([4, 5, 6])),
            32,
        )

    def test_length(self) -> None:
        self.assertAlmostEqual(
            Vector([3, 4]).length(),
            5.0,
        )

    def test_getitem(self) -> None:
        vector = Vector([10, 20, 30])

        self.assertEqual(vector[0], 10)
        self.assertEqual(vector[2], 30)

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
        first_vector = Vector(list(range(100)))
        second_vector = Vector(list(range(100, 200)))
        expected_vector = Vector([i + (i + 100) for i in range(100)])

        self.assertEqual(first_vector + second_vector, expected_vector)

    def test_subtract_large_vectors(self) -> None:
        first_vector = Vector(list(range(200, 300)))
        second_vector = Vector(list(range(100)))
        expected_vector = Vector([200 for _ in range(100)])

        self.assertEqual(first_vector - second_vector, expected_vector)

    def test_scalar_multiply_large_vector(self) -> None:
        vector = Vector(list(range(100)))
        expected_vector = Vector([i * 3 for i in range(100)])

        self.assertEqual(vector * 3, expected_vector)

    def test_dot_product_large_vectors(self) -> None:
        first_vector = Vector([1 for _ in range(100)])
        second_vector = Vector([2 for _ in range(100)])

        self.assertEqual(first_vector.dot(second_vector), 200)

    def test_large_vector_length(self) -> None:
        vector = Vector([1 for _ in range(100)])

        self.assertAlmostEqual(vector.length(), math.sqrt(100))


if __name__ == "__main__":
    unittest.main()
