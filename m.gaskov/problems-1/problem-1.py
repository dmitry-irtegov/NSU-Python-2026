import unittest


def cumulative_sums(seq):
    sums = [0]
    for x in seq:
        sums.append(sums[-1] + x)
    return sums


class TestCumulativeSums(unittest.TestCase):
    def test_example(self):
        self.assertEqual(cumulative_sums([1, 2, 3]), [0, 1, 3, 6])

    def test_empty(self):
        self.assertEqual(cumulative_sums([]), [0])

    def test_floats(self):
        self.assertEqual(cumulative_sums([0.5, 1.5, 2.0]), [0, 0.5, 2.0, 4.0])

    def test_strings(self):
        with self.assertRaises(TypeError):
            cumulative_sums(["a", "b", "c"])

    def test_large(self):
        self.assertEqual(cumulative_sums([1] * 10000), [i for i in range(0, 10001)])


if __name__ == "__main__":
    unittest.main()