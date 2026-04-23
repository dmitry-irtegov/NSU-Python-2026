import io
import unittest
from contextlib import redirect_stderr, redirect_stdout
from unittest.mock import patch

import problem5


class TestGeneratePrimes(unittest.TestCase):
    def test_n_2(self):
        self.assertEqual(problem5.generate_primes(2), [2])

    def test_n_10(self):
        self.assertEqual(problem5.generate_primes(10), [2, 3, 5, 7])

    def test_n_30(self):
        self.assertEqual(problem5.generate_primes(30), [2, 3, 5, 7, 11, 13, 17, 19, 23, 29])

    def test_big_complex_example(self):
        self.assertEqual(problem5.generate_primes(100), [
            2, 3, 5, 7, 11, 13, 17, 19, 23, 29,
            31, 37, 41, 43, 47, 53, 59, 61, 67,
            71, 73, 79, 83, 89, 97
        ])

    def test_all_numbers_are_prime(self):
        primes = problem5.generate_primes(100)
        for x in primes:
            for d in range(2, int(x ** 0.5) + 1):
                self.assertNotEqual(x % d, 0)

    def test_all_numbers_not_greater_than_n(self):
        n = 100
        primes = problem5.generate_primes(n)
        self.assertTrue(all(2 <= x <= n for x in primes))

    def test_invalid_n_raises_value_error(self):
        with self.assertRaises(ValueError):
            problem5.generate_primes(0)

    def test_invalid_type_raises_type_error(self):
        with self.assertRaises(TypeError):
            problem5.generate_primes("10")


class TestFormatPrimes(unittest.TestCase):
    def test_format_empty(self):
        self.assertEqual(problem5.format_primes([]), "")

    def test_format_basic(self):
        self.assertEqual(problem5.format_primes([2, 3, 5, 7]), "2 3 5 7")

    def test_invalid_type_raises(self):
        with self.assertRaises(TypeError):
            problem5.format_primes("2 3 5 7")


class TestMainIO(unittest.TestCase):
    def run_main_capture(self, input_behavior):
        out_buf = io.StringIO()
        err_buf = io.StringIO()

        if isinstance(input_behavior, BaseException):
            side_effect = input_behavior
        else:
            def side_effect():
                return input_behavior

        with (
            patch("builtins.input", side_effect=side_effect),
            redirect_stdout(out_buf),
            redirect_stderr(err_buf)
        ):
            problem5.main()

        return out_buf.getvalue(), err_buf.getvalue()

    def test_main_empty_input_defaults_to_10(self):
        out, err = self.run_main_capture("")
        self.assertEqual(err, "")
        self.assertEqual(out, "2 3 5 7\n")

    def test_main_custom_n_30(self):
        out, err = self.run_main_capture("30")
        self.assertEqual(err, "")
        self.assertEqual(out, "2 3 5 7 11 13 17 19 23 29\n")

    def test_main_n_1_prints_nothing(self):
        out, err = self.run_main_capture("1")
        self.assertEqual(out, "")
        self.assertNotEqual(err, "")

    def test_main_invalid_input_logs(self):
        out, err = self.run_main_capture("abc")
        self.assertEqual(out, "")
        self.assertNotEqual(err, "")

    def test_main_keyboard_interrupt_logs(self):
        out, err = self.run_main_capture(KeyboardInterrupt())
        self.assertEqual(out, "")
        self.assertIn("Interrupted by user.", err)


if __name__ == "__main__":
    unittest.main()