import unittest
from math import isqrt
import time

from lab_1 import get_triples
class MyTestCase(unittest.TestCase):
    def test(self):
        triples = set(get_triples(10**4))
        self.assertEqual(len(triples), 12467)
        for triple in triples:
            self.assertEqual(triple[0]**2 + triple[1]**2, triple[2]**2)


    def test_speed(self):
        def get_triples_stupid(n):
            res = []
            for a in range(1, n):
                for b in range(a + 1, n):
                    c2 = a ** 2 + b ** 2
                    c = isqrt(c2)
                    if c ** 2 == c2 and c < n:
                        res.append((a, b, c))
            return res

        def get_time(func, max):
            start = time.time()
            func(max)
            end = time.time()
            return end - start


        time_of_stupid = get_time(get_triples_stupid, 2*10**4)
        time_of_my = get_time(get_triples, 2*10**4)
        self.assertTrue(time_of_my * 10 < time_of_stupid)





if __name__ == '__main__':
    unittest.main()
