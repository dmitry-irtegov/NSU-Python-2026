import unittest
from Set import Combinations


class TestCombinations(unittest.TestCase):
    def test_basic(self):
        c = Combinations([1, 2], 2)

        expected = [
            (1, 1),
            (1, 2),
            (2, 1),
            (2, 2),
        ]

        result = []
        for _ in range(4):
            result.append(c.current())
            c.next()

        self.assertEqual(result, expected)

    def test_cycle(self):
        c = Combinations([1, 2], 2)

        for _ in range(4):
            c.next()

        self.assertEqual(c.current(), (1, 1))

    def test_single_element(self):
        c = Combinations([5], 3)

        for _ in range(5):
            self.assertEqual(c.current(), (5, 5, 5))
            c.next()

    def test_strings(self):
        c = Combinations(["a", "b"], 2)

        self.assertEqual(c.current(), ("a", "a"))
        c.next()
        self.assertEqual(c.current(), ("a", "b"))

    def test_mixed_types(self):
        c = Combinations([1, "a"], 2)

        self.assertEqual(c.current(), (1, 1))
        c.next()
        self.assertEqual(c.current(), (1, "a"))

    def test_n_equals_1(self):
        c = Combinations([1, 2, 3], 1)

        expected = [(1,), (2,), (3,)]

        result = []
        for _ in range(3):
            result.append(c.current())
            c.next()

        self.assertEqual(result, expected)

    def test_invalid_arr(self):
        with self.assertRaises(ValueError):
            Combinations([], 2)

    def test_invalid_n(self):
        with self.assertRaises(ValueError):
            Combinations([1, 2], 0)

    def test_large_n(self):
        c = Combinations([1, 2], 3)

        expected = [
            (1, 1, 1),
            (1, 1, 2),
            (1, 2, 1),
            (1, 2, 2),
            (2, 1, 1),
            (2, 1, 2),
            (2, 2, 1),
            (2, 2, 2),
        ]

        result = []
        for _ in range(8):
            result.append(c.current())
            c.next()

        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
