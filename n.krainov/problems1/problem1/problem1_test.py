import unittest
from problem1 import cumulative_sum

class TestCumulativeSum(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(cumulative_sum([]), [0])

    def test_single_positive(self):
        self.assertEqual(cumulative_sum([5]), [0, 5])

    def test_single_negative(self):
        self.assertEqual(cumulative_sum([-3]), [0, -3])

    def test_multiple_positive(self):
        self.assertEqual(cumulative_sum([1, 2, 3]), [0, 1, 3, 6])

    def test_mixed_signs(self):
        self.assertEqual(cumulative_sum([1, -2, 3]), [0, 1, -1, 2])

    def test_all_zeros(self):
        self.assertEqual(cumulative_sum([0, 0, 0]), [0, 0, 0, 0])

    def test_empty(self):
        self.assertEqual(cumulative_sum([]), [0])


if __name__ == '__main__':
    unittest.main()