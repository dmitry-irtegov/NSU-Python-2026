import unittest

from problem5 import primes_up_to


class PrimesUpToTests(unittest.TestCase):
    @staticmethod
    def is_prime(n: int) -> bool:
        if n < 2:
            return False
        return all(n % d != 0 for d in range(2, int(n ** 0.5) + 1))

    def test_less_than_two(self):
        self.assertEqual(primes_up_to(-10), [])
        self.assertEqual(primes_up_to(0), [])
        self.assertEqual(primes_up_to(1), [])

    def test_two(self):
        self.assertEqual(primes_up_to(2), [2])

    def test_thirty(self):
        self.assertEqual(primes_up_to(30), [2, 3, 5, 7, 11, 13, 17, 19, 23, 29])

    def test_returns_sorted_unique_primes_only(self):
        result = primes_up_to(50)

        self.assertEqual(result, sorted(result))
        self.assertEqual(len(result), len(set(result)))
        self.assertTrue(all(self.is_prime(number) for number in result))

    def test_large_n(self):
        result = primes_up_to(100000)

        self.assertEqual(len(result), 9592)
        self.assertEqual(result, sorted(result))
        self.assertEqual(len(result), len(set(result)))
        self.assertTrue(all(self.is_prime(number) for number in result))
        self.assertEqual(result[-1], 99991)
        self.assertNotIn(100000, result)


if __name__ == "__main__":
    unittest.main()
