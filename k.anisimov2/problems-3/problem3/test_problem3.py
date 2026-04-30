import math
import unittest

import problem3


class TestVector(unittest.TestCase):
    def test_create_and_dimension(self):
        v = problem3.Vector([1, 2, 3])
        self.assertEqual(v.dimension(), 3)

    def test_get_item(self):
        v = problem3.Vector([10, 20, 30])
        self.assertEqual(v[0], 10)
        self.assertEqual(v[1], 20)
        self.assertEqual(v[2], 30)

    def test_addition(self):
        v1 = problem3.Vector([1, 2, 3])
        v2 = problem3.Vector([4, 5, 6])
        self.assertEqual(v1 + v2, problem3.Vector([5, 7, 9]))

    def test_subtraction(self):
        v1 = problem3.Vector([10, 20, 30])
        v2 = problem3.Vector([1, 2, 3])
        self.assertEqual(v1 - v2, problem3.Vector([9, 18, 27]))

    def test_multiply_by_constant_right(self):
        v = problem3.Vector([1, 2, 3])
        self.assertEqual(v * 3, problem3.Vector([3, 6, 9]))

    def test_multiply_by_constant_left(self):
        v = problem3.Vector([1, 2, 3])
        self.assertEqual(3 * v, problem3.Vector([3, 6, 9]))

    def test_dot_product_method(self):
        v1 = problem3.Vector([1, 2, 3])
        v2 = problem3.Vector([4, 5, 6])
        self.assertEqual(v1.dot(v2), 32)

    def test_dot_product_operator(self):
        v1 = problem3.Vector([1, 2, 3])
        v2 = problem3.Vector([4, 5, 6])
        self.assertEqual(v1 * v2, 32)

    def test_length(self):
        v = problem3.Vector([3, 4])
        self.assertEqual(v.length(), 5)

    def test_length_for_3d_vector(self):
        v = problem3.Vector([1, 2, 2])
        self.assertEqual(v.length(), 3)

    def test_equality_true(self):
        self.assertEqual(problem3.Vector([1, 2, 3]), problem3.Vector([1, 2, 3]))

    def test_equality_false(self):
        self.assertNotEqual(problem3.Vector([1, 2, 3]), problem3.Vector([1, 2, 4]))

    def test_string_representation(self):
        v = problem3.Vector([1, 2, 3])
        self.assertEqual(str(v), "(1, 2, 3)")

    def test_repr(self):
        v = problem3.Vector([1, 2, 3])
        self.assertEqual(repr(v), "Vector([1, 2, 3])")

    def test_big_complex_example(self):
        v1 = problem3.Vector([2, -3, 5, 0, 7])
        v2 = problem3.Vector([-1, 4, 2, 8, -6])

        self.assertEqual(v1 + v2, problem3.Vector([1, 1, 7, 8, 1]))
        self.assertEqual(v1 - v2, problem3.Vector([3, -7, 3, -8, 13]))
        self.assertEqual(v1 * 2, problem3.Vector([4, -6, 10, 0, 14]))
        self.assertEqual(-3 * v2, problem3.Vector([3, -12, -6, -24, 18]))
        self.assertEqual(v1.dot(v2), -46)
        self.assertEqual(v1 * v2, -46)
        self.assertEqual(v1[0], 2)
        self.assertEqual(v1[4], 7)
        self.assertEqual(v1.dimension(), 5)
        self.assertAlmostEqual(v1.length(), math.sqrt(87))


if __name__ == "__main__":
    unittest.main()