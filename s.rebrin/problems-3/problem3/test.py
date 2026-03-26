import unittest

from vector import Vector


class TestVector(unittest.TestCase):
    def test_add_vector(self):
        self.assertEqual(Vector([1, 2, 3]) + Vector([4, 5, 6]), Vector([5, 7, 9]))

    def test_add_scalar(self):
        self.assertEqual(Vector([1, 2, 3]) + 1, Vector([2, 3, 4]))

    def test_radd(self):
        self.assertEqual(1 + Vector([1, 2, 3]), Vector([2, 3, 4]))

    def test_sub_vector(self):
        self.assertEqual(Vector([5, 7, 9]) - Vector([1, 2, 3]), Vector([4, 5, 6]))

    def test_sub_scalar(self):
        self.assertEqual(Vector([5, 6, 7]) - 1, Vector([4, 5, 6]))

    def test_rsub(self):
        self.assertEqual(10 - Vector([1, 2, 3]), Vector([9, 8, 7]))

    def test_mul_scalar(self):
        self.assertEqual(Vector([1, 2, 3]) * 2, Vector([2, 4, 6]))

    def test_rmul_scalar(self):
        self.assertEqual(2 * Vector([1, 2, 3]), Vector([2, 4, 6]))

    def test_mul_zero(self):
        self.assertEqual(Vector([1, 2, 3]) * 0, Vector([0, 0, 0]))

    def test_mul_negative(self):
        self.assertEqual(Vector([1, -2, 3]) * -1, Vector([-1, 2, -3]))

    def test_mul_empty_vector(self):
        self.assertEqual(Vector([]) * 5, Vector([]))

    def test_dot(self):
        self.assertEqual(Vector([1, 2, 3]).dot(Vector([4, 5, 6])), 32)

    def test_length(self):
        self.assertAlmostEqual(Vector([3, 4]).length(), 5.0)

    def test_index(self):
        self.assertEqual(Vector([10, 20, 30])[1], 20)

    def test_len(self):
        self.assertEqual(len(Vector([1, 2, 3])), 3)

    def test_eq(self):
        self.assertTrue(Vector([1, 2]) == Vector([1, 2]))
        self.assertFalse(Vector([1, 2]) == Vector([2, 1]))

    def test_zero_vector(self):
        v = Vector([0, 0, 0])
        self.assertEqual(v.length(), 0.0)
        self.assertEqual(v.dot(v), 0)

    def test_empty_vector(self):
        v = Vector([])
        self.assertEqual(len(v), 0)
        self.assertEqual(v.length(), 0.0)

    def test_single_element(self):
        v = Vector([5])
        self.assertEqual(v.length(), 5.0)

    def test_invalid_element_type(self):
        with self.assertRaises(TypeError):
            Vector([1, 2, "a"])

    def test_add_wrong_type(self):
        with self.assertRaises(TypeError):
            _ = Vector([1, 2, 3]) + "abc"

    def test_sub_wrong_type(self):
        with self.assertRaises(TypeError):
            _ = Vector([1, 2, 3]) - [1, 2, 3]

    def test_dot_wrong_type(self):
        with self.assertRaises(TypeError):
            Vector([1, 2, 3]).dot(123)

    def test_different_sizes(self):
        with self.assertRaises(ValueError):
            Vector([1, 2]) + Vector([1])

    def test_index_wrong_type(self):
        with self.assertRaises(TypeError):
            _ = Vector([1, 2, 3])["a"]

    def test_out_of_bounds(self):
        with self.assertRaises(IndexError):
            _ = Vector([1, 2, 3])[10]

    def test_mul_wrong_type(self):
        with self.assertRaises(TypeError):
            _ = Vector([1, 2, 3]) * "abc"

    def test_rmul_wrong_type(self):
        with self.assertRaises(TypeError):
            _ = "abc" * Vector([1, 2, 3])


if __name__ == "__main__":
    unittest.main()
