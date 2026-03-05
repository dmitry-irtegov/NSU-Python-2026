import unittest


def clip_sequence(seq, a, b):
    if a > b:
        raise ValueError("Lower bound 'a' must be <= upper bound 'b'")

    res = []
    for x in seq:
        if x < a:
            res.append(a)
        elif x > b:
            res.append(b)
        else:
            res.append(x)
    return res


class TestClipSequence(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(clip_sequence([1, 2, 3, 10], 2, 5), [2, 2, 3, 5])

    def test_empty(self):
        self.assertEqual(clip_sequence([], 10, 15), [])

    def test_all_inside(self):
        self.assertEqual(clip_sequence([2, 3, 4], 2, 5), [2, 3, 4])

    def test_all_below(self):
        self.assertEqual(clip_sequence([-5, -1, 0], 1, 3), [1, 1, 1])

    def test_all_above(self):
        self.assertEqual(clip_sequence([7, 8], 1, 3), [3, 3])

    def test_floats(self):
        self.assertEqual(clip_sequence([0.1, 2.5, 10.0], 1.0, 3.0), [1.0, 2.5, 3.0])

    def test_equal_bounds(self):
        self.assertEqual(clip_sequence([1, 2, 3], 2, 2), [2, 2, 2])

    def test_large(self):
        self.assertEqual(
            clip_sequence(list(range(1, 100)), 10, 90),
            [10] * 10 + list(range(11, 90)) + [90] * 10
        )

    def test_strings(self):
        self.assertEqual(clip_sequence(["aa", "bb", "cc", "dd"], "bb", "cc"), ["bb", "bb", "cc", "cc"])

    def test_invalid_types(self):
        with self.assertRaises(TypeError):
            clip_sequence(["aa", "bb", "cc", "dd"], 1, 2)

    def test_raises_if_a_greater_than_b(self):
        with self.assertRaises(ValueError):
            clip_sequence([1, 2, 3], 10, 5)


if __name__ == "__main__":
    unittest.main()