import unittest

from problem1 import cumulative_sum


class TestCumulativeSum(unittest.TestCase):
    def test_example(self):
        self.assertEqual(cumulative_sum([1, 2, 3]), [0, 1, 3, 6])

    def test_empty(self):
        self.assertEqual(cumulative_sum([]), [0])

    def test_single_element(self):
        self.assertEqual(cumulative_sum([5]), [0, 5])

    def test_all_zeros(self):
        self.assertEqual(cumulative_sum([0, 0, 0]), [0, 0, 0, 0])

    def test_negative_numbers(self):
        self.assertEqual(cumulative_sum([-1, -2, -3]), [0, -1, -3, -6])

    def test_mixed_numbers(self):
        self.assertEqual(cumulative_sum([5, -2, 0, 3]), [0, 5, 3, 3, 6])

if __name__ == '__main__':
    unittest.main()