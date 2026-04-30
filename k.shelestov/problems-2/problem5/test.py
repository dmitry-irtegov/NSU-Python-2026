import unittest
from problem5 import return_prime_list


def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True


class TestPrimes(unittest.TestCase):

    def test_small(self):
        self.assertEqual(return_prime_list(10), [2, 3, 5, 7])

    def test_zero(self):
        self.assertEqual(return_prime_list(0), [])

    def test_negative(self):
        self.assertEqual(return_prime_list(-100), [])

    def test_one(self):
        self.assertEqual(return_prime_list(1), [])

    def test_two(self):
        self.assertEqual(return_prime_list(2), [2])

    def test_medium(self):
        self.assertEqual(
            return_prime_list(30),
            [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
        )

    def test_large_consistency(self):
        res = return_prime_list(100)

        self.assertTrue(all(is_prime(x) for x in res))

        expected = [x for x in range(2, 101) if is_prime(x)]
        self.assertEqual(res, expected)


if __name__ == "__main__":
    unittest.main()