import unittest
from problem5 import prime_factors

class TestPrimeFactors(unittest.TestCase):

    def test_standard_numbers(self):
        self.assertEqual(prime_factors(12), [(2, 2), (3, 1)])
        self.assertEqual(prime_factors(100), [(2, 2), (5, 2)])
        self.assertEqual(prime_factors(360), [(2, 3), (3, 2), (5, 1)])

    def test_prime_numbers(self):
        self.assertEqual(prime_factors(2), [(2, 1)])
        self.assertEqual(prime_factors(7), [(7, 1)])
        self.assertEqual(prime_factors(13), [(13, 1)])

    def test_edge_cases(self):
        self.assertEqual(prime_factors(1), [])
        self.assertEqual(prime_factors(0), [])
        self.assertEqual(prime_factors(-10), [])

    def test_large_numbers(self):
        self.assertEqual(prime_factors(9409), [(97, 2)])
        self.assertEqual(prime_factors(104729), [(104729, 1)])

if __name__ == "__main__":
    unittest.main()