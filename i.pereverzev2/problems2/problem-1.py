import unittest
import random

def get_triples(n):
    return [
        (x, y, z)
        for x in range(1, n + 1)
        for y in range(x + 1, n + 1)
        for z in range(y + 1, n + 1)
        if x**2 + y**2 == z**2
    ]

class TestPy(unittest.TestCase):
    def setUp(self):
        random.seed(42)

    def test_1(self):
        self.assertEqual(get_triples(1), [])

    def test_5(self):
        self.assertEqual(get_triples(5), [(3, 4, 5)])

    def test_10(self):
        self.assertEqual(get_triples(10), [(3, 4, 5), (6, 8, 10)])

    def test_0(self):
        self.assertEqual(get_triples(0), [])

    def test_neg(self):
        self.assertEqual(get_triples(-1), [])

    def test_rnd_math(self):
        n = random.randint(50, 100)
        res = get_triples(n)
        for x, y, z in res:
            self.assertEqual(x**2 + y**2, z**2)

    def test_rnd_range(self):
        n = random.randint(101, 150)
        res = get_triples(n)
        for x, y, z in res:
            self.assertTrue(z <= n)

    def test_rnd_order(self):
        n = random.randint(20, 30)
        res = get_triples(n)
        for x, y, z in res:
            self.assertTrue(x < y < z)

if __name__ == '__main__':
    unittest.main()