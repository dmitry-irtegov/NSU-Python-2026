#!/usr/bin/python
import unittest

def clip(seq, a, b):
    res = []
    for num in seq:
        num = max(a, num)
        num = min(b, num)
        res.append(num)
    return res


class TestClip(unittest.TestCase):

    def test_positive_bounds(self):
        self.assertEqual(clip([5, 15, 25], 10, 20), [10, 15, 20])

    def test_negative_bounds(self):
        self.assertEqual(clip([-20, -7, 0], -10, -5), [-10, -7, -5])

    def test_spanning_zero(self):
        self.assertEqual(clip([-100, 0, 100], -5, 5), [-5, 0, 5])

    def test_large_numbers(self):
        self.assertEqual(clip([1e20, -1e20], -1e10, 1e10), [1e10, -1e10])

    def test_boundaries_exact(self):
        self.assertEqual(clip([0, 50, 100], 0, 100), [0, 50, 100])

    def test_all_clipped(self):
        self.assertEqual(clip([1, 2, 3], 10, 20), [10, 10, 10])

    def test_empty(self):
        self.assertEqual(clip([], -5, 5), [])

    def test_floats(self):
        self.assertEqual(clip([0.1, 2.0], 0.5, 1.5), [0.5, 1.5])


if __name__ == "__main__":
    unittest.main()