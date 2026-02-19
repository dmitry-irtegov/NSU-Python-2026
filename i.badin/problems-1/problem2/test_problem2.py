import unittest

from problem2 import clip_numbers


class TestClipNumbers(unittest.TestCase):
    def test_mixed_values_are_clipped(self):
        self.assertEqual(clip_numbers([-5, 1, 3, 4.5, 10, 15.5], 0, 5), [0, 1, 3, 4.5, 5, 5])

    def test_values_inside_boundaries_not_changed(self):
        self.assertEqual(clip_numbers([2, 3, 4], 1, 5), [2, 3, 4])

    def test_all_values_become_boundary_when_a_equals_b(self):
        self.assertEqual(clip_numbers([1, 2, 3], 2, 2), [2, 2, 2])

    def test_empty_sequence_returns_empty_list(self):
        self.assertEqual(clip_numbers([], -1, 1), [])

    def test_raises_value_error_when_lower_bound_is_greater_than_upper(self):
        with self.assertRaises(ValueError):
            clip_numbers([1, 2, 3], 5, 2)

if __name__ == "__main__":
    unittest.main()
