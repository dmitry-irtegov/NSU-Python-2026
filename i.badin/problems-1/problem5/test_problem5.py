import unittest

from problem5 import factorize


class TestFactorize(unittest.TestCase):
    def test_example(self):
        self.assertEqual(factorize(12), [[2, 2], [3, 1]])

    def test_prime_number(self):
        self.assertEqual(factorize(13), [[13, 1]])

    def test_power_of_prime(self):
        self.assertEqual(factorize(32), [[2, 5]])

    def test_one(self):
        self.assertEqual(factorize(1), [])

    def test_multiple_prime_factors(self):
        self.assertEqual(factorize(360), [[2, 3], [3, 2], [5, 1]])

    def test_invalid_number(self):
        with self.assertRaises(ValueError):
            factorize(0)


if __name__ == "__main__":
    unittest.main()
