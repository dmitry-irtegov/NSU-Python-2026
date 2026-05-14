import random
import unittest

def pithagoras_triplets(n):
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
    
    def test_zero(self):
        self.assertListEqual(pithagoras_triplets(0), [])

    def test_negative(self):
        self.assertListEqual(pithagoras_triplets(-1), [])

    def test_five(self):
        self.assertListEqual(pithagoras_triplets(5), [(3, 4, 5)])

    def test_random_range(self):
        n = random.randint(45, 100)
        res = pithagoras_triplets(n)
        for x, y, z in res:
            self.assertEqual(x**2 + y**2, z**2)

    def test_members_le_than_n(self):
        n = random.randint(40, 90)
        res = pithagoras_triplets(n)
        for x, y, z in res:
            self.assertTrue(z <= n)

    def test_order_works(self):
        n = random.randint(30, 80)
        res = pithagoras_triplets(n)
        for x, y, z in res:
            self.assertTrue(x < y < z)


if __name__ == '__main__':
    unittest.main()