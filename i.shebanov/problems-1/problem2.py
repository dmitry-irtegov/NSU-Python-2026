#!/usr/bin/python3

import unittest
from random import randint


def narrow_list(arr, lower_bound, upper_bound):
    result = []
    for x in arr:
        if x > upper_bound:
            result.append(upper_bound)
        elif x < lower_bound:
            result.append(lower_bound)
        else:
            result.append(x)
    return result


class TestNarrowList(unittest.TestCase):

    def setUp(self):
        self.RANDOM_MAX = 10000
        self.RANDOM_MIN = -10000
        self.original_list = [
            randint(self.RANDOM_MIN, self.RANDOM_MAX)
            for _ in range(1000)
        ]
        self.lower_bound = randint(self.RANDOM_MIN, self.RANDOM_MAX)
        self.upper_bound = randint(self.lower_bound, self.RANDOM_MAX)

        self.new_list = narrow_list(
            self.original_list,
            self.lower_bound,
            self.upper_bound
        )

    def test_length(self):
        self.assertEqual(len(self.new_list), len(self.original_list))

    def test_values(self):
        self.assertTrue(
            all(self.lower_bound <= x <= self.upper_bound for x in self.new_list)
        )

    def test_same_values(self):
        self.assertTrue(
            all(
                self.new_list[i] == self.original_list[i]
                for i in range(len(self.new_list))
                if self.lower_bound <= self.original_list[i] <= self.upper_bound
            )
        )


if __name__ == "__main__":
    unittest.main()
