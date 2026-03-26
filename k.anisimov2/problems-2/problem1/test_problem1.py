import io
import unittest
from contextlib import redirect_stderr, redirect_stdout
from unittest.mock import patch

import problem1


class TestGenerateTriples(unittest.TestCase):
    def test_n_5(self):
        self.assertEqual(problem1.generate_pythagorean_triples(5), [(3, 4, 5)])

    def test_n_10_contains_expected(self):
        triples = problem1.generate_pythagorean_triples(10)
        self.assertIn((3, 4, 5), triples)
        self.assertIn((6, 8, 10), triples)

    def test_all_values_not_greater_than_n(self):
        n = 30
        triples = problem1.generate_pythagorean_triples(n)
        self.assertTrue(all(1 <= x <= y < z <= n for x, y, z in triples))

    def test_each_is_pythagorean(self):
        triples = problem1.generate_pythagorean_triples(50)
        self.assertTrue(all(x * x + y * y == z * z for x, y, z in triples))

    def test_invalid_n_raises_value_error(self):
        with self.assertRaises(ValueError):
            problem1.generate_pythagorean_triples(0)

    def test_invalid_type_raises_type_error(self):
        with self.assertRaises(TypeError):
            problem1.generate_pythagorean_triples("10")


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
            problem1.main()

        return out_buf.getvalue(), err_buf.getvalue()

    def test_main_empty_input_defaults_to_10(self):
        out, err = self.run_main_capture("")
        self.assertEqual(err, "")
        self.assertIn("(3, 4, 5)", out)

    def test_main_custom_n_5(self):
        out, err = self.run_main_capture("5")
        self.assertEqual(err, "")
        self.assertEqual(out, "(3, 4, 5)\n")

    def test_main_invalid_input_logs(self):
        out, err = self.run_main_capture("abc")
        self.assertEqual(out, "")
        self.assertTrue(err.startswith("Input error:"))

    def test_main_invalid_start_logs(self):
        out, err = self.run_main_capture("0")
        self.assertEqual(out, "")
        self.assertNotEqual(err, "")

    def test_main_keyboard_interrupt_logs(self):
        out, err = self.run_main_capture(KeyboardInterrupt())
        self.assertEqual(out, "")
        self.assertIn("Interrupted by user.", err)


if __name__ == "__main__":
    unittest.main()