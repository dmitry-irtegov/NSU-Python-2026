import unittest
from lab_5 import get_simple
from functools import reduce
from random import randint, seed

class MyTestCase(unittest.TestCase):
    def test_simple(self):
        cases = [
            (52, [[2, 2], [13, 1]]),
            (100, [[2, 2], [5, 2]]),
            (5, [[5, 1]]),
            (3, [[3, 1]]),
            (7, [[7, 1]]),
            (6, [[2, 1], [3, 1]])
        ]
        for (num, ans) in cases:
            res = get_simple(num)
            self.assertEqual(num, reduce(lambda acc, x: acc * (x[0] ** x[1]), res, 1))


    def test_negative_numbers(self):
        self.assertEqual(get_simple(-4), [[2, 2]])
        self.assertEqual(get_simple(-6), [[2, 1], [3, 1]])
        self.assertEqual(get_simple(-12), [[2, 2], [3, 1]])

    def test_number_one(self):
        self.assertEqual(get_simple(1), [])

    def test_zero(self):
        self.assertEqual(get_simple(0), [])

    def test_large_prime(self):
        large_prime = 999983
        result = get_simple(large_prime)
        self.assertEqual(result, [[large_prime, 1]])

    def test_large_power_of_two(self):
        result = get_simple(2 ** 20)
        self.assertEqual(result, [[2, 20]])

    def test_random(self):
        seed(1)
        for _ in range(100):
            num = randint(10**4, 10**6)
            ans = get_simple(num)
            summ = 1
            for pair in ans:
                summ *= pair[0] ** pair[1]
            self.assertEqual(num, summ)



if __name__ == '__main__':
    unittest.main()
