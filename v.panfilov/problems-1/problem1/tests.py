import unittest
from problem1 import cumulative_sums


class TestSums(unittest.TestCase):
    def test_1(self):
        self.assertEqual(cumulative_sums([1, 2, 3]), [0, 1, 3, 6])


    def test_2(self):
        self.assertEqual(cumulative_sums([0]), [0, 0])

    def test_3(self):
        self.assertEqual(cumulative_sums([]), [0])

    def test_4(self):
        self.assertEqual(cumulative_sums(range(1, 18)), [0, 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 105, 120, 136, 153])

    def test_5(self):
        self.assertEqual(cumulative_sums([1.5, 2.5, 3.5]), [0, 1.5, 4.0, 7.5])

    def test_6(self):
        self.assertEqual(cumulative_sums([-1, -2, -3]), [0, -1, -3, -6])

    def test_7(self):
        self.assertEqual(cumulative_sums([1, -1, 2, -2]), [0, 1, 0, 2, 0])

    def test_8(self):
        self.assertEqual(cumulative_sums([42]), [0, 42])

    def test_9(self):
        self.assertEqual(cumulative_sums([0, 0, 0]), [0, 0, 0, 0])

if __name__ == "__main__":
    unittest.main()
