import io
import math
import random
import unittest
from contextlib import redirect_stderr, redirect_stdout
from unittest.mock import patch

import problem5


def is_prime(n):
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    r = int(math.isqrt(n))
    d = 3
    while d <= r:
        if n % d == 0:
            return False
        d += 2
    return True


class TestFactorize(unittest.TestCase):
    def test_example(self):
        self.assertEqual(problem5.factorize(12), [[2, 2], [3, 1]])

    def test_prime(self):
        self.assertEqual(problem5.factorize(13), [[13, 1]])

    def test_power_of_prime(self):
        self.assertEqual(problem5.factorize(32), [[2, 5]])

    def test_one_and_zero_and_negative(self):
        with redirect_stderr(io.StringIO()):
            self.assertEqual(problem5.factorize(1), [])
            self.assertEqual(problem5.factorize(0), [])
            self.assertEqual(problem5.factorize(-7), [])

    def test_invariants_random_inputs(self):
        rng = random.Random(2026)
        for _ in range(200):
            n = rng.randint(2, 200_000)
            res = problem5.factorize(n)
            self.assertTrue(res)

            primes = [p for p, _ in res]
            exps = [k for _, k in res]

            self.assertEqual(primes, sorted(primes))
            self.assertEqual(len(primes), len(set(primes)))
            self.assertTrue(all(is_prime(p) for p in primes))
            self.assertTrue(all(k >= 1 for k in exps))

            prod = 1
            for p, k in res:
                prod *= p**k
            self.assertEqual(prod, n)

    def test_large_number_invariants(self):
        n = 999_983
        res = problem5.factorize(n)
        prod = 1
        for p, k in res:
            self.assertTrue(is_prime(p))
            self.assertGreaterEqual(k, 1)
            prod *= p**k
        self.assertEqual(prod, n)


class TestMainIO(unittest.TestCase):
    def run_main_capture(self, input_behavior):
        out_buf = io.StringIO()
        err_buf = io.StringIO()

        if isinstance(input_behavior, Exception):
            side_effect = input_behavior
        else:
            def side_effect():
                return input_behavior

        with patch("builtins.input", side_effect=side_effect), redirect_stdout(out_buf), redirect_stderr(err_buf):
            problem5.main()

        return out_buf.getvalue(), err_buf.getvalue()

    def test_output_for_12(self):
        out, err = self.run_main_capture("12")
        self.assertEqual(out, "[[2, 2], [3, 1]]\n")
        self.assertEqual(err, "")

    def test_whitespace_input_ok(self):
        out, err = self.run_main_capture("   12   ")
        self.assertEqual(out, "[[2, 2], [3, 1]]\n")
        self.assertEqual(err, "")

    def test_invalid_zero_logs_to_stderr_and_no_stdout(self):
        out, err = self.run_main_capture("0")
        self.assertEqual(out, "")
        self.assertNotEqual(err, "")

    def test_invalid_one_logs_to_stderr_and_no_stdout(self):
        out, err = self.run_main_capture("1")
        self.assertEqual(out, "")
        self.assertNotEqual(err, "")

    def test_invalid_negative_logs_to_stderr_and_no_stdout(self):
        out, err = self.run_main_capture("-7")
        self.assertEqual(out, "")
        self.assertNotEqual(err, "")

    def test_non_integer_logs_to_stderr(self):
        out, err = self.run_main_capture("abc")
        self.assertEqual(out, "")
        self.assertNotEqual(err, "")

    def test_float_like_logs_to_stderr(self):
        out, err = self.run_main_capture("3.14")
        self.assertEqual(out, "")
        self.assertNotEqual(err, "")

    def test_empty_string_logs_to_stderr(self):
        out, err = self.run_main_capture("")
        self.assertEqual(out, "")
        self.assertNotEqual(err, "")

    def test_eof_logs_to_stderr(self):
        out, err = self.run_main_capture(EOFError("EOF"))
        self.assertEqual(out, "")
        self.assertNotEqual(err, "")

    def test_stderr_never_pollutes_stdout_on_errors(self):
        bad_inputs = ["0", "1", "-1", "hello", "1e3", "", "   ", "++2", "--2"]
        for s in bad_inputs:
            out, err = self.run_main_capture(s)
            self.assertEqual(out, "")
            self.assertNotEqual(err, "")

    def test_random_valid_inputs_stdout_matches_factorize(self):
        rng = random.Random(7)
        for _ in range(50):
            n = rng.randint(2, 50_000)
            expected = str(problem5.factorize(n)) + "\n"
            out, err = self.run_main_capture(str(n))
            self.assertEqual(err, "")
            self.assertEqual(out, expected)


if __name__ == "__main__":
    unittest.main()