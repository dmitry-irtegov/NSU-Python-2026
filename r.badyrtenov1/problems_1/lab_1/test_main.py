#!/usr/bin/env python3

import unittest
from itertools import accumulate
from random import randint, seed
from sys import maxsize

from main import cumulative_sums


class TestCumulativeSums(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        seed(0)

    def test_empty(self):
        self.assertEqual(cumulative_sums([]), [0])

    def test_example(self):
        self.assertEqual(cumulative_sums([1, 2, 3]), [0, 1, 3, 6])

    def test_random(self):
        for _ in range(5000):
            length = randint(0, 5000)
            nums = [randint(-maxsize, maxsize) for _ in range(length)]
            self.assertEqual(cumulative_sums(nums), [0] + list(accumulate(nums)))


if __name__ == "__main__":
    unittest.main()
