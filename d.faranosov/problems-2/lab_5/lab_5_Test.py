import unittest
from math import isqrt
from lab_5 import get_simple

class MyTestCase(unittest.TestCase):
    def test_simple(self):
        simples = get_simple(100)
        ans = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
        self.assertEqual(simples, ans)

    def test_hard(self):
        cnt_simples = 78498
        def check_simple(simple):
            return all(simple % x != 0 for x in range(2, isqrt(simple)))

        simples = get_simple(10**6)
        self.assertEqual(len(simples), cnt_simples)

        for simple in simples:
            self.assertTrue(check_simple(simple))

if __name__ == '__main__':
    unittest.main()
