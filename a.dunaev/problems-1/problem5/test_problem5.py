import importlib.util
import math
import pathlib
import unittest


MODULE_PATH = pathlib.Path(__file__).with_name("problem5.py")
SPEC = importlib.util.spec_from_file_location("problem5", MODULE_PATH)
problem5 = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(problem5)


class Problem5Tests(unittest.TestCase):
    def test_zero_returns_empty_list(self) -> None:
        self.assertEqual(problem5.to_prime(0), [])

    def test_one_returns_empty_list(self) -> None:
        self.assertEqual(problem5.to_prime(1), [])

    def test_factorization_of_composite_number(self) -> None:
        self.assertEqual(problem5.to_prime(60), [[2, 2], [3, 1], [5, 1]])

    def test_factorization_of_prime_power(self) -> None:
        self.assertEqual(problem5.to_prime(1024), [[2, 10]])

    def test_large_number_does_not_overflow_and_reconstructs_source(self) -> None:
        num = 321413252345246436413513513254

        factors = problem5.to_prime(num)

        reconstructed = math.prod(prime ** power for prime, power in factors)
        self.assertEqual(reconstructed, num)
        self.assertEqual(factors, [[2, 1], [6959, 1], [201069653, 1], [114852490973348201, 1]])
        self.assertTrue(all(problem5._is_prime(prime) for prime, _ in factors))


if __name__ == "__main__":
    unittest.main()
