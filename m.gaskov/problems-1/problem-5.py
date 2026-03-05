import unittest


def prime_factorization(n: int) -> list[list[int]]:
    if not isinstance(n, int):
        raise TypeError("n must be int")
    if n <= 1:
        raise ValueError("n must be > 1")

    res = []
    p = 2
    while p * p <= n:
        k = 0
        while n % p == 0:
            n //= p
            k += 1
        if k:
            res.append([p, k])
        p += 1
    if n > 1:
        res.append([n, 1])
    return res


class TestPrimeFactorization(unittest.TestCase):
    def test_example_12(self):
        self.assertEqual(prime_factorization(12), [[2, 2], [3, 1]])

    def test_prime_number(self):
        self.assertEqual(prime_factorization(13), [[13, 1]])

    def test_mixed(self):
        self.assertEqual(prime_factorization(360), [[2, 3], [3, 2], [5, 1]])

    def test_invalid_n_le_1(self):
        for x in [1, 0, -10]:
            with self.subTest(x=x):
                with self.assertRaises(ValueError):
                    prime_factorization(x)


if __name__ == "__main__":
    unittest.main()