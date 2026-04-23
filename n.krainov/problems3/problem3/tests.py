import unittest
from problem3 import Vector

class TestVectorInit(unittest.TestCase):
    def test_zero_vector_by_default(self):
        v = Vector(3)
        self.assertEqual(v[0], 0)
        self.assertEqual(v[1], 0)
        self.assertEqual(v[2], 0)

    def test_len(self):
        self.assertEqual(len(Vector(5)), 5)
        self.assertEqual(len(Vector(1)), 1)

    def test_from_list(self):
        v = Vector.from_list([1, 2, 3])
        self.assertEqual(v[0], 1)
        self.assertEqual(v[1], 2)
        self.assertEqual(v[2], 3)

    def test_from_list_does_not_share_memory(self):
        nums = [1, 2, 3]
        v = Vector.from_list(nums)
        nums[0] = 99
        self.assertEqual(v[0], 1)

    def test_from_list_len(self):
        v = Vector.from_list([10, 20])
        self.assertEqual(len(v), 2)

    def test_setitem_getitem(self):
        v = Vector(3)
        v[1] = 42
        self.assertEqual(v[1], 42)

    def test_str_representation(self):
        v = Vector.from_list([1, 2, 3])
        self.assertEqual(str(v), "( 1, 2, 3 )")

    def test_str_single_element(self):
        v = Vector.from_list([7])
        self.assertEqual(str(v), "( 7 )")

    def test_str_negative_elements(self):
        v = Vector.from_list([-1, -2])
        self.assertEqual(str(v), "( -1, -2 )")


class TestVectorAddition(unittest.TestCase):
    def test_basic_addition(self):
        v1 = Vector.from_list([1, 2, 3])
        v2 = Vector.from_list([4, 5, 6])
        result = v1 + v2
        self.assertEqual(result, Vector.from_list([5, 7, 9]))

    def test_addition_with_zeros(self):
        v1 = Vector.from_list([1, 2, 3])
        v2 = Vector(3)
        self.assertEqual(v1 + v2, v1)

    def test_addition_with_negatives(self):
        v1 = Vector.from_list([1, -2, 3])
        v2 = Vector.from_list([-1, 2, -3])
        self.assertEqual(v1 + v2, Vector(3))

    def test_addition_does_not_mutate_operands(self):
        v1 = Vector.from_list([1, 2, 3])
        v2 = Vector.from_list([4, 5, 6])
        _ = v1 + v2
        self.assertEqual(v1, Vector.from_list([1, 2, 3]))
        self.assertEqual(v2, Vector.from_list([4, 5, 6]))

    def test_addition_commutativity(self):
        v1 = Vector.from_list([1, 2, 3])
        v2 = Vector.from_list([4, 5, 6])
        self.assertEqual(v1 + v2, v2 + v1)


class TestVectorSubtraction(unittest.TestCase):
    def test_basic_subtraction(self):
        v1 = Vector.from_list([5, 7, 9])
        v2 = Vector.from_list([1, 2, 3])
        self.assertEqual(v1 - v2, Vector.from_list([4, 5, 6]))

    def test_subtraction_self(self):
        v = Vector.from_list([1, 2, 3])
        self.assertEqual(v - v, Vector(3))

    def test_subtraction_does_not_mutate_operands(self):
        v1 = Vector.from_list([5, 7, 9])
        v2 = Vector.from_list([1, 2, 3])
        _ = v1 - v2
        self.assertEqual(v1, Vector.from_list([5, 7, 9]))
        self.assertEqual(v2, Vector.from_list([1, 2, 3]))

    def test_subtraction_result_negative(self):
        v1 = Vector.from_list([1, 2])
        v2 = Vector.from_list([3, 5])
        self.assertEqual(v1 - v2, Vector.from_list([-2, -3]))


class TestVectorMultiplication(unittest.TestCase):
    def test_mul_integer_scalar(self):
        v = Vector.from_list([1, 2, 3])
        self.assertEqual(v * 3, Vector.from_list([3, 6, 9]))

    def test_mul_float_scalar(self):
        v = Vector.from_list([2, 4])
        result = v * 0.5
        self.assertAlmostEqual(result[0], 1.0)
        self.assertAlmostEqual(result[1], 2.0)

    def test_mul_zero_scalar(self):
        v = Vector.from_list([1, 2, 3])
        self.assertEqual(v * 0, Vector(3))

    def test_mul_negative_scalar(self):
        v = Vector.from_list([1, -2, 3])
        self.assertEqual(v * -1, Vector.from_list([-1, 2, -3]))

    def test_rmul(self):
        v = Vector.from_list([1, 2, 3])
        self.assertEqual(3 * v, v * 3)

    def test_mul_does_not_mutate_vector(self):
        v = Vector.from_list([1, 2, 3])
        _ = v * 5
        self.assertEqual(v, Vector.from_list([1, 2, 3]))


class TestVectorDotProduct(unittest.TestCase):
    def test_basic_dot(self):
        v1 = Vector.from_list([1, 2, 3])
        v2 = Vector.from_list([4, 5, 6])
        self.assertEqual(v1.dot(v2), 32)  # 1*4 + 2*5 + 3*6 = 32

    def test_dot_with_zero_vector(self):
        v1 = Vector.from_list([1, 2, 3])
        v2 = Vector(3)
        self.assertEqual(v1.dot(v2), 0)

    def test_dot_commutativity(self):
        v1 = Vector.from_list([1, 2, 3])
        v2 = Vector.from_list([4, 5, 6])
        self.assertEqual(v1.dot(v2), v2.dot(v1))

    def test_dot_with_negatives(self):
        v1 = Vector.from_list([1, -1])
        v2 = Vector.from_list([1, 1])
        self.assertEqual(v1.dot(v2), 0)

    def test_dot_unit_vectors(self):
        v1 = Vector.from_list([1, 0, 0])
        v2 = Vector.from_list([0, 1, 0])
        self.assertEqual(v1.dot(v2), 0)

    def test_dot_1d(self):
        v1 = Vector.from_list([7])
        v2 = Vector.from_list([3])
        self.assertEqual(v1.dot(v2), 21)


class TestVectorEquality(unittest.TestCase):
    def test_equal_vectors(self):
        v1 = Vector.from_list([1, 2, 3])
        v2 = Vector.from_list([1, 2, 3])
        self.assertTrue(v1 == v2)

    def test_not_equal_vectors(self):
        v1 = Vector.from_list([1, 2, 3])
        v2 = Vector.from_list([1, 2, 4])
        self.assertFalse(v1 == v2)

    def test_equal_zero_vectors(self):
        self.assertTrue(Vector(4) == Vector(4))

    def test_reflexivity(self):
        v = Vector.from_list([1, 2, 3])
        self.assertTrue(v == v)

    def test_symmetry(self):
        v1 = Vector.from_list([1, 2])
        v2 = Vector.from_list([1, 2])
        self.assertEqual(v1 == v2, v2 == v1)

    def test_differs_by_first_element(self):
        v1 = Vector.from_list([0, 2, 3])
        v2 = Vector.from_list([1, 2, 3])
        self.assertFalse(v1 == v2)


if __name__ == "__main__":
    unittest.main()