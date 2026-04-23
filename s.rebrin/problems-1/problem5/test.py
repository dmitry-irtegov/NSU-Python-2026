import unittest

from main import get_primes


class TestGetPrimes(unittest.TestCase):
    def check_factorization(self, N: int):
        original = N
        primes = get_primes(N)

        for a, b in primes:
            self.assertEqual(original % (a**b), 0)
            original //= a**b

        self.assertEqual(original, 1)

    def test_180(self):
        self.check_factorization(180)

    def test_composite_large(self):
        self.check_factorization(6 * 7 * 8 * 9 * 11 * 13 * 15)

    def test_prime_number(self):
        self.check_factorization(461)

    def test_zero(self):
        with self.assertRaises(ValueError):
            get_primes(0)

    def test_negative(self):
        with self.assertRaises(ValueError):
            get_primes(-5)


if __name__ == "__main__":
    unittest.main()
