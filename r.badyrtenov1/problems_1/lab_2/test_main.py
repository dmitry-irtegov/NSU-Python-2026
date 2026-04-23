#!/usr/bin/env python3

import unittest
from random import randint, uniform, seed
from sys import float_info

from main import clip_nums


class TestCumulativeSums(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        seed(0)

    def test_empty(self):
        self.assertEqual(clip_nums([], 0, 10), [])

    def test_example(self):
        self.assertEqual(clip_nums([1e20, -1e20], -1e10, 1e10), [1e10, -1e10])

    def test_random(self):
        for _ in range(5000):
            length = randint(0, 5000)
            nums = [uniform(float_info.min, float_info.max) for _ in range(length)]
            b1, b2 = uniform(float_info.min, float_info.max), uniform(float_info.min, float_info.max)
            a, b = min(b1, b2), max(b1, b2)
            self.assertEqual(clip_nums(nums, a, b), [max(a, min(num, b)) for num in nums])


if __name__ == "__main__":
    unittest.main()
