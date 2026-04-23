import unittest
import math


def primes_up_to(n: int) -> list[int]:
    return [
        x
        for x in range(2, n + 1)
        if all(x % d != 0 for d in range(2, math.isqrt(x) + 1))
    ]


class TestPrimesUpTo(unittest.TestCase):
    def test_ten(self) -> None:
        self.assertEqual(primes_up_to(10), [2, 3, 5, 7])

    def test_small(self) -> None:
        self.assertEqual(primes_up_to(2), [2])

    def test_negative(self) -> None:
        self.assertEqual(primes_up_to(-10), [])

    def test_zero(self) -> None:
        self.assertEqual(primes_up_to(0), [])

    def test_one(self) -> None:
        self.assertEqual(primes_up_to(1), [])

    def test_large(self) -> None:
        n = 1000
        primes = primes_up_to(n)

        self.assertEqual(len(primes), 168)
        self.assertEqual(len(primes), len(set(primes)))
        self.assertEqual(primes, sorted(primes))

        for x in primes:
            self.assertTrue(2 <= x <= n)
            self.assertTrue(all(x % d != 0 for d in range(2, math.isqrt(x) + 1)))


if __name__ == "__main__":
    unittest.main()