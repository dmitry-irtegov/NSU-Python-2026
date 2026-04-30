import unittest


def gen_primes(n):
    return [
        prime
        for prime in range(2, n + 1)
        if sum([prime % i == 0 for i in range(2, int(prime**0.5) + 1)]) == 0
    ]


class TestPrimes(unittest.TestCase):
    def test_up_to_10(self):
        self.assertEqual(gen_primes(10), [2, 3, 5, 7])

    def test_up_to_20(self):
        self.assertEqual(gen_primes(20), [2, 3, 5, 7, 11, 13, 17, 19])

    def test_negative(self):
        self.assertEqual(gen_primes(-5), [])

    def test_zero(self):
        self.assertEqual(gen_primes(0), [])

    def test_one(self):
        self.assertEqual(gen_primes(1), [])

    def test_two(self):
        self.assertEqual(gen_primes(2), [2])

    def test_last_prime_in_50(self):
        self.assertEqual(gen_primes(50)[-1], 47)

    def test_count_primes_up_to_100(self):
        self.assertEqual(len(gen_primes(100)), 25)


if __name__ == "__main__":
    unittest.main()
