import unittest
from vector import Vector


class TestVector(unittest.TestCase):
    def test_add_vector(self):
        self.assertEqual(Vector([1, 2, 3]) + Vector([4, 5, 6]), Vector([5, 7, 9]))

    def test_add_scalar(self):
        self.assertEqual(Vector([1, 2, 3]) + 1, Vector([2, 3, 4]))

    def test_sub_vector(self):
        self.assertEqual(Vector([5, 7, 9]) - Vector([1, 2, 3]), Vector([4, 5, 6]))

    def test_dot(self):
        self.assertEqual(Vector([1, 2, 3]).dot(Vector([4, 5, 6])), 32)

    def test_length(self):
        self.assertAlmostEqual(Vector([3, 4]).vector_len(), 5.0)

    def test_index(self):
        self.assertEqual(Vector([1, 2, 3])[1], 2)

    def test_invalid_size(self):
        with self.assertRaises(ValueError):
            Vector([1, 2]) + Vector([1])


if __name__ == "__main__":
    unittest.main()
