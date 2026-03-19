import unittest
from problem5 import prime_factors

class TestFactor(unittest.TestCase):
    def test_0(self):
        self.assertRaises(ValueError, prime_factors, 0)

    def test_1(self):
        self.assertEqual(prime_factors(1), [[1, 1]])

    def test_2(self):
        self.assertEqual(prime_factors(1000000000000), [[2, 12], [5, 12], [1, 1]])

    def test_3(self):
        self.assertRaises(ValueError, prime_factors, -1000000000000)

    def test_4(self):
        self.assertRaises(ValueError, prime_factors, 'text')

    def test_zero(self):
        self.assertRaises(ValueError, prime_factors, 0)

    def test_negative(self):
        self.assertRaises(ValueError, prime_factors, -100)

if __name__ == "__main__":
    unittest.main()