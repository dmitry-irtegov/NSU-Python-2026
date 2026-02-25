import io
import random
import unittest
from contextlib import redirect_stdout, redirect_stderr
from unittest.mock import patch

import problem3


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
            problem3.main()

        return out_buf.getvalue(), err_buf.getvalue()

    def test_output_for_3_stdout_only(self):
        out, err = self.run_main_capture("3")
        self.assertEqual(out, "3 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1\n")
        self.assertEqual(err, "")

    def test_output_for_1_stdout_only(self):
        out, err = self.run_main_capture("1")
        self.assertEqual(out, "1\n")
        self.assertEqual(err, "")

    def test_no_trailing_arrow_or_spaces(self):
        out, err = self.run_main_capture("8")
        self.assertEqual(out, "8 -> 4 -> 2 -> 1\n")
        self.assertFalse(out.strip().endswith("->"))
        self.assertEqual(err, "")

    def test_whitespace_input_is_ok(self):
        out, err = self.run_main_capture("   7   ")
        self.assertTrue(out.startswith("7"))
        self.assertTrue(out.endswith("\n"))
        self.assertEqual(err, "")

    def test_invalid_zero_logs_to_stderr(self):
        out, err = self.run_main_capture("0")
        self.assertEqual(out, "")
        self.assertIn("Invalid number for Collatz", err)
        self.assertIn("0", err)

    def test_invalid_negative_logs_to_stderr(self):
        out, err = self.run_main_capture("-12")
        self.assertEqual(out, "")
        self.assertIn("Invalid number for Collatz", err)
        self.assertIn("-12", err)

    def test_non_integer_logs_to_stderr(self):
        out, err = self.run_main_capture("abc")
        self.assertEqual(out, "")
        self.assertIn("Input error", err)

    def test_float_like_logs_to_stderr(self):
        out, err = self.run_main_capture("3.14")
        self.assertEqual(out, "")
        self.assertIn("Input error", err)

    def test_empty_string_logs_to_stderr(self):
        out, err = self.run_main_capture("")
        self.assertEqual(out, "")
        self.assertIn("Input error", err)

    def test_eof_logs_to_stderr(self):
        out, err = self.run_main_capture(EOFError("EOF"))
        self.assertEqual(out, "")
        self.assertIn("Input error", err)

    def test_random_valid_inputs_stdout_has_correct_format(self):
        rng = random.Random(123)
        for _ in range(50):
            n = rng.randint(1, 10_000)
            out, err = self.run_main_capture(str(n))
            self.assertEqual(err, "")
            self.assertTrue(out.endswith("\n"))
            self.assertTrue(out.startswith(str(n)))
            self.assertTrue(out.endswith("1\n"))

            parts = out.strip().split(" -> ")
            self.assertEqual(int(parts[0]), n)
            self.assertEqual(int(parts[-1]), 1)
            for p in parts:
                self.assertRegex(p, r"^-?\d+$")

    def test_stderr_never_pollutes_stdout_on_errors(self):
        error_inputs = ["0", "-1", "hello", "1e3", "", "   ", "++2", "--2"]
        for s in error_inputs:
            out, err = self.run_main_capture(s)
            self.assertEqual(out, "")
            self.assertNotEqual(err, "")