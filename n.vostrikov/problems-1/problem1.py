import unittest


def cumulative_sums(seq):
    sums = [0]
    for num in seq:
        sums.append(sums[-1] + num)
    return sums


class TestSums(unittest.TestCase):
    def test_positive(self):
        self.assertEqual(cumulative_sums([1, 2, 3]), [0, 1, 3, 6])

    def test_negative(self):
        self.assertEqual(cumulative_sums([-1, -2, -3]), [0, -1, -3, -6])

    def test_mixed(self):
        self.assertEqual(cumulative_sums([1, -2, 3]), [0, 1, -1, 2])

    def test_empty_list(self):
        self.assertEqual(cumulative_sums([]), [0])

    def test_large_list(self):
        self.assertEqual(cumulative_sums([1] * 1000), [i for i in range(0, 1001)])


if __name__ == "__main__":
    unittest.main()