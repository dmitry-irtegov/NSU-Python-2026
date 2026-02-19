import random
import unittest
from lab_5 import get_simple
from functools import reduce
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


    def test_hard(self):
        for num in range(1, 10):
            num = random.randint(10**5, 10**7)
            res = get_simple(num)
            self.assertEqual(num, reduce(lambda acc, x: acc * (x[0] ** x[1]), res, 1))


if __name__ == '__main__':
    unittest.main()
