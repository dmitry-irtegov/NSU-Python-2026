import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch

import problem3


class TestCollatz(unittest.TestCase):
    def test_example(self):
        self.assertEqual(problem3.collatz(3), [3, 10, 5, 16, 8, 4, 2, 1])

    def test_one(self):
        self.assertEqual(problem3.collatz(1), [1])

    def test_even(self):
        self.assertEqual(problem3.collatz(8), [8, 4, 2, 1])

    def test_invalid(self):
        self.assertEqual(problem3.collatz(0), [])
        self.assertEqual(problem3.collatz(-7), [])


class TestOutputFormat(unittest.TestCase):
    def run_main_and_capture(self, user_input: str) -> str:
        buf = io.StringIO()
        with patch("builtins.input", return_value=user_input), redirect_stdout(buf):
            problem3.main()
        return buf.getvalue()

    def test_output_for_3(self):
        out = self.run_main_and_capture("3")
        self.assertEqual(out, "3 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1\n")

    def test_output_for_1(self):
        out = self.run_main_and_capture("1")
        self.assertEqual(out, "1\n")

    def test_output_for_invalid_zero(self):
        out = self.run_main_and_capture("0")
        self.assertEqual(out, "")

    def test_no_trailing_arrow_or_spaces(self):
        out = self.run_main_and_capture("8")
        self.assertEqual(out, "8 -> 4 -> 2 -> 1\n")
        self.assertFalse(out.strip().endswith("->"))


if __name__ == "__main__":
    unittest.main()
