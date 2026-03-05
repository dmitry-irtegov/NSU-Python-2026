import unittest
from problem2 import apply_boundaries


class TestApplyBoundariesNormal(unittest.TestCase):
    def test_all_within_bounds(self):
        self.assertEqual(apply_boundaries([1, 2, 3], 0, 5), [1, 2, 3])

    def test_clamp_below_a(self):
        self.assertEqual(apply_boundaries([-10, -5, 0], 0, 5), [0, 0, 0])

    def test_clamp_above_b(self):
        self.assertEqual(apply_boundaries([6, 7, 100], 0, 5), [5, 5, 5])

    def test_mixed_clamping(self):
        self.assertEqual(apply_boundaries([-3, 2, 8], 0, 5), [0, 2, 5])

    def test_exact_boundaries_not_clamped(self):
        self.assertEqual(apply_boundaries([0, 5], 0, 5), [0, 5])

    def test_a_equals_b(self):
        self.assertEqual(apply_boundaries([1, 3, 5], 3, 3), [3, 3, 3])

    def test_negative_boundaries(self):
        self.assertEqual(apply_boundaries([-10, -5, 0, 5], -7, -2), [-7, -5, -2, -2])

    def test_float_values(self):
        self.assertEqual(apply_boundaries([0.5, 1.5, 2.5], 1.0, 2.0), [1.0, 1.5, 2.0])

    def test_float_boundaries(self):
        self.assertEqual(apply_boundaries([1, 2, 3], 1.5, 2.5), [1.5, 2, 2.5])


class TestApplyBoundariesEdgeCases(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(apply_boundaries([], 0, 10), [])

    def test_single_element_within(self):
        self.assertEqual(apply_boundaries([5], 0, 10), [5])

    def test_single_element_below(self):
        self.assertEqual(apply_boundaries([-1], 0, 10), [0])

    def test_single_element_above(self):
        self.assertEqual(apply_boundaries([99], 0, 10), [10])

    def test_returns_list(self):
        result = apply_boundaries([1, 2, 3], 0, 5)
        self.assertIsInstance(result, list)

    def test_original_list_not_modified(self):
        original = [1, 2, 3]
        apply_boundaries(original, 0, 2)
        self.assertEqual(original, [1, 2, 3])


class TestApplyBoundariesInvalidInput(unittest.TestCase):
    def test_a_greater_than_b_raises(self):
        with self.assertRaises(ValueError):
            apply_boundaries([1, 2, 3], 10, 5)

    def test_a_greater_than_b_message(self):
        with self.assertRaises(ValueError) as ctx:
            apply_boundaries([1, 2, 3], 10, 5)
        self.assertEqual(str(ctx.exception), "a can't be greater than b")

    def test_a_equals_b_does_not_raise(self):
        try:
            apply_boundaries([1], 5, 5)
        except ValueError:
            self.fail("ValueError raised when a == b")