import unittest

def generate_primes(n: int):
    return [
        x for x in range(2, n + 1)
        if all(x % d != 0 for d in range(2, int(x ** 0.5) + 1))
    ]

class TestGeneratePrimes(unittest.TestCase):

    def test_one(self):
        self.assertEqual(generate_primes(1), [])

    def test_basic_primes(self):
        self.assertEqual(generate_primes(10), [2, 3, 5, 7])

    def test_single_prime(self):
        self.assertEqual(generate_primes(2), [2])

    def test_medium_range(self):
        self.assertEqual(generate_primes(100), [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97])

    def test_no_primes(self):
        self.assertEqual(generate_primes(0), [])

if __name__ == "__main__":
    unittest.main()