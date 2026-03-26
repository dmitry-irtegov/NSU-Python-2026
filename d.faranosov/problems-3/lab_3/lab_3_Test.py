import unittest
from lab_3 import Vector

class MyTestCase(unittest.TestCase):

    def test_add_float_vectors(self):
        v1 = Vector([1.5, 2.3, 3.7])
        v2 = Vector([4.1, 5.9, 6.2])
        result = v1 + v2
        self.assertEqual(result, Vector([5.6, 8.2, 9.9]))

    def test_add_vectors_large_size(self):
        v1 = Vector(list(range(100)))
        v2 = Vector(list(range(100, 200)))
        expected = [i + (i + 100) for i in range(100)]
        result = v1 + v2
        self.assertEqual(result, Vector(expected))

    def test_add_commutative(self):
        v1 = Vector([1, 2, 3])
        v2 = Vector([4, 5, 6])
        self.assertEqual((v1 + v2), (v2 + v1))

    def test_add_different_sizes_raises_error(self):
        v1 = Vector([1, 2, 3])
        v2 = Vector([4, 5, 6, 7])
        with self.assertRaises(ValueError) as context:
            v1 + v2
        self.assertEqual(str(context.exception), "Adding vectors with different sizes")

    def test_add_does_not_modify_original(self):
        v1 = Vector([1, 2, 3])
        v2 = Vector([4, 5, 6])
        v1_copy = Vector(v1.elements)
        v2_copy = Vector(v2.elements)
        v1 + v2
        self.assertEqual(v1.elements, v1_copy.elements)
        self.assertEqual(v2.elements, v2_copy.elements)

    def test_sub_float_vectors(self):
        v1 = Vector([5.6, 8.2, 9.9])
        v2 = Vector([4.1, 5.9, 6.2])
        result = v1 - v2
        self.assertEqual(result, Vector([1.5, 2.3, 3.7]))

    def test_sub_vectors_large_size(self):
        v1 = Vector(list(range(100, 200)))
        v2 = Vector(list(range(100)))
        expected = [i + 100 - i for i in range(100)]
        result = v1 - v2
        self.assertEqual(result, Vector(expected))

    def test_sub_not_commutative(self):
        v1 = Vector([1, 2, 3])
        v2 = Vector([4, 5, 6])
        self.assertNotEqual((v1 - v2), (v2 - v1))

    def test_sub_self_minus_self(self):
        v = Vector([1, 2, 3, 4, 5])
        result = v - v
        self.assertEqual(result, Vector([0, 0, 0, 0, 0]))

    def test_sub_different_sizes_raises_error(self):
        v1 = Vector([1, 2, 3])
        v2 = Vector([4, 5, 6, 7])
        with self.assertRaises(ValueError) as context:
            v1 - v2
        self.assertEqual(str(context.exception), "sub vectors with different sizes")

    def test_sub_does_not_modify_original(self):
        v1 = Vector([1, 2, 3])
        v2 = Vector([4, 5, 6])
        v1_copy = Vector(v1.elements)
        v2_copy = Vector(v2.elements)
        v1 - v2
        self.assertEqual(v1.elements, v1_copy.elements)
        self.assertEqual(v2.elements, v2_copy.elements)

    def test_dot_product_float_vectors(self):
        v1 = Vector([1.5, 2.3, 3.7])
        v2 = Vector([4.1, 5.9, 6.2])
        result = v1 * v2
        expected = 1.5 * 4.1 + 2.3 * 5.9 + 3.7 * 6.2
        self.assertAlmostEqual(result, expected)

    def test_dot_product_commutative(self):
        v1 = Vector([1, 2, 3])
        v2 = Vector([4, 5, 6])
        self.assertEqual(v1 * v2, v2 * v1)

    def test_dot_product_different_sizes_raises_error(self):
        v1 = Vector([1, 2, 3])
        v2 = Vector([4, 5, 6, 7])
        with self.assertRaises(ValueError) as context:
            v1 * v2
        self.assertEqual(str(context.exception), "mul vectors with different sizes")

    def test_scalar_multiplication_float(self):
        v = Vector([1, 2, 3, 4, 5])
        result = v * 2.5
        self.assertEqual(result, Vector([2.5, 5.0, 7.5, 10.0, 12.5]))

    def test_scalar_multiplication_does_not_modify_original(self):
        v = Vector([1, 2, 3])
        v_copy = Vector(v.elements)
        v * 2.0
        self.assertEqual(v.elements, v_copy.elements)

    def test_dot_product_large_vectors(self):
        v1 = Vector(list(range(1000)))
        v2 = Vector(list(range(1000, 2000)))
        expected = sum(i * (i + 1000) for i in range(1000))
        result = v1 * v2
        self.assertEqual(result, expected)

    def test_scalar_multiplication_large_vector(self):
        v = Vector(list(range(1000)))
        result = v * 0.5
        expected = tuple([i * 0.5 for i in range(1000)])
        self.assertEqual(result.elements, expected)

    def test_different_vectors(self):
        v1 = Vector([1, 2, 3])
        v2 = Vector([4, 5, 6])
        self.assertFalse(v1 == v2)

    def test_equal_vectors_with_float(self):
        v1 = Vector([1.5, 2.3, 3.7])
        v2 = Vector([1.5, 2.3, 3.7])
        self.assertTrue(v1 == v2)

    def test_equal_vectors_large_size(self):
        v1 = Vector(list(range(1000)))
        v2 = Vector(list(range(1000)))
        self.assertTrue(v1 == v2)

    def test_different_sizes(self):
        v1 = Vector([1, 2, 3])
        v2 = Vector([1, 2, 3, 4])
        self.assertFalse(v1 == v2)

    def test_compare_with_non_vector(self):
        v = Vector([1, 2, 3])
        self.assertFalse(v == [1, 2, 3])
        self.assertFalse(v == "vector")
        self.assertFalse(v == 42)
        self.assertFalse(v is None)

    def test_reflexive(self):
        v = Vector([1, 2, 3])
        self.assertTrue(v == v)

    def test_symmetric(self):
        v1 = Vector([1, 2, 3])
        v2 = Vector([1, 2, 3])
        self.assertTrue(v1 == v2 and v2 == v1)

    def test_equal_after_operations(self):
        v1 = Vector([1, 2, 3])
        v2 = Vector([4, 5, 6])
        v3 = v1 + v2
        v4 = Vector([5, 7, 9])
        self.assertTrue(v3 == v4)

if __name__ == '__main__':
    unittest.main()
