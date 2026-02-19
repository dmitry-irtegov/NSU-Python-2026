import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch

import problem5


class TestFactorize(unittest.TestCase):
    def test_example(self):
        self.assertEqual(problem5.factorize(12), [[2, 2], [3, 1]])

    def test_prime(self):
        self.assertEqual(problem5.factorize(13), [[13, 1]])

    def test_power_of_prime(self):
        self.assertEqual(problem5.factorize(32), [[2, 5]])

    def test_one_and_zero_and_negative(self):
        self.assertEqual(problem5.factorize(1), [])
        self.assertEqual(problem5.factorize(0), [])
        self.assertEqual(problem5.factorize(-7), [])


class TestOutputFormat(unittest.TestCase):
    def run_main_and_capture(self, user_input: str) -> str:
        buf = io.StringIO()
        with patch("builtins.input", return_value=user_input), redirect_stdout(buf):
            problem5.main()
        return buf.getvalue()

    def test_output_for_12(self):
        out = self.run_main_and_capture("12")
        self.assertEqual(out, "[[2, 2], [3, 1]]\n")


if __name__ == "__main__":
    unittest.main()
