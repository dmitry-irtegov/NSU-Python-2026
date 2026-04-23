import unittest

def prime_factors(n):
    factors = []
    d = 2

    while d * d <= n:
        count = 0

        while n % d == 0:
            n //= d
            count += 1

        if count > 0:
            factors.append([d, count])

        d += 1

    if n > 1:
        factors.append([n, 1])

    return factors

class TestPrimeFactors(unittest.TestCase):

    def test_prime_number(self):
        self.assertEqual(prime_factors(13), [[13, 1]])

    def test_composite_number(self):
        self.assertEqual(prime_factors(12), [[2, 2], [3, 1]])

    def test_power_of_prime(self):
        self.assertEqual(prime_factors(16), [[2, 4]])

    def test_two_primes(self):
        self.assertEqual(prime_factors(15), [[3, 1], [5, 1]])

    def test_one(self):
        self.assertEqual(prime_factors(1), [])


if __name__ == "__main__":
    unittest.main()