import unittest
from problem5 import get_primes


class TestPrimeGenerator(unittest.TestCase):
    def test_get_primes_basic(self) -> None:
        self.assertEqual(get_primes(10), [2, 3, 5, 7])
        self.assertEqual(get_primes(20), [2, 3, 5, 7, 11, 13, 17, 19])
        self.assertEqual(get_primes(30), [2, 3, 5, 7, 11, 13, 17, 19, 23, 29])

    def test_get_primes_boundary_cases(self) -> None:
        self.assertEqual(get_primes(2), [2])
        self.assertEqual(get_primes(1), [])
        self.assertEqual(get_primes(0), [])
        self.assertEqual(get_primes(-5), [])

    def test_get_primes_large_number(self) -> None:
        primes_up_to_100: list[int] = get_primes(100)
        self.assertEqual(len(primes_up_to_100), 25)
        self.assertEqual(primes_up_to_100[-1], 97)


if __name__ == '__main__':
    unittest.main()