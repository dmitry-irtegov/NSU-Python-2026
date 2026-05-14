import unittest

from problem2 import clip_sequence


class TestClipSequence(unittest.TestCase):
    def test_mixed_values(self):
        self.assertEqual(
            clip_sequence([1, 5, 10, -3, 7], 2, 8),
            [2, 5, 8, 2, 7],
        )

    def test_all_below_lower(self):
        self.assertEqual(clip_sequence([0, 1, 2], 5, 10), [5, 5, 5])

    def test_all_above_upper(self):
        self.assertEqual(clip_sequence([20, 30, 40], 0, 10), [10, 10, 10])

    def test_empty(self):
        self.assertEqual(clip_sequence([], 0, 10), [])

    def test_bounds_equal(self):
        self.assertEqual(
            clip_sequence([1, 2, 3, 4, 5], 3, 3),
            [3, 3, 3, 3, 3],
        )

    def test_values_on_boundaries(self):
        self.assertEqual(
            clip_sequence([-5, 0, 5, 10], -5, 10),
            [-5, 0, 5, 10],
        )

    def test_negative_range(self):
        self.assertEqual(
            clip_sequence([-10, -5, 0, 5, 10], -3, 3),
            [-3, -3, 0, 3, 3],
        )

    def test_floats(self):
        self.assertEqual(
            clip_sequence([1.5, 2.7, 3.2, 4.8], 2.0, 4.0),
            [2.0, 2.7, 3.2, 4.0],
        )

    def test_invalid_range_raises(self):
        with self.assertRaises(ValueError):
            clip_sequence([1, 2, 3], 5, 2)


if __name__ == "__main__":
    unittest.main()
