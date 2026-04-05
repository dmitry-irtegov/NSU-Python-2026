import io
import os
import tempfile
import unittest
from contextlib import redirect_stderr, redirect_stdout
from unittest.mock import patch

import problem4


class TestLoadPiDigits(unittest.TestCase):
    def test_load_digits_only(self):
        with tempfile.NamedTemporaryFile("w+", delete=False, encoding="utf-8") as tmp:
            tmp.write("3.1415\n9265\r\n")
            name = tmp.name

        try:
            self.assertEqual(problem4.load_pi_digits(name), "314159265")
        finally:
            os.remove(name)

    def test_invalid_filename_type_raises(self):
        with self.assertRaises(TypeError):
            problem4.load_pi_digits(123)

    def test_empty_filename_raises(self):
        with self.assertRaises(ValueError):
            problem4.load_pi_digits("")

    def test_file_without_digits_raises(self):
        with tempfile.NamedTemporaryFile("w+", delete=False, encoding="utf-8") as tmp:
            tmp.write("abc...\nxyz")
            name = tmp.name

        try:
            with self.assertRaises(ValueError):
                problem4.load_pi_digits(name)
        finally:
            os.remove(name)


class TestFindAllOccurrences(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(problem4.find_all_occurrences("314159265358", "15"), [3])

    def test_multiple_occurrences(self):
        self.assertEqual(problem4.find_all_occurrences("14154151415", "1415"), [0, 7])

    def test_overlapping_occurrences(self):
        self.assertEqual(problem4.find_all_occurrences("1111", "11"), [0, 1, 2])

    def test_no_occurrences(self):
        self.assertEqual(problem4.find_all_occurrences("31415926", "777"), [])

    def test_invalid_pattern_empty_raises(self):
        with self.assertRaises(ValueError):
            problem4.find_all_occurrences("31415926", "")

    def test_invalid_pattern_non_digit_raises(self):
        with self.assertRaises(ValueError):
            problem4.find_all_occurrences("31415926", "14a")

    def test_invalid_text_type_raises(self):
        with self.assertRaises(TypeError):
            problem4.find_all_occurrences(31415926, "14")


class TestFormatSearchResult(unittest.TestCase):
    def test_zero_results(self):
        self.assertEqual(
            problem4.format_search_result([]),
            "Found 0 results.\nPositions:"
        )

    def test_less_than_five_results(self):
        self.assertEqual(
            problem4.format_search_result([2, 10, 15]),
            "Found 3 results.\nPositions: 2 10 15"
        )

    def test_more_than_five_results(self):
        self.assertEqual(
            problem4.format_search_result([1, 2, 3, 4, 5, 6, 7]),
            "Found 7 results.\nPositions: 1 2 3 4 5 ..."
        )


class TestMainIO(unittest.TestCase):
    def run_main_capture(self, pi_content, input_behavior):
        out_buf = io.StringIO()
        err_buf = io.StringIO()

        with tempfile.TemporaryDirectory() as tmpdir:
            pi_path = os.path.join(tmpdir, "pi.txt")
            with open(pi_path, "w", encoding="utf-8") as f:
                f.write(pi_content)

            old_cwd = os.getcwd()
            os.chdir(tmpdir)
            try:
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
                    problem4.main()
            finally:
                os.chdir(old_cwd)

        return out_buf.getvalue(), err_buf.getvalue()

    def test_main_ok(self):
        out, err = self.run_main_capture("3.1415926535", "15")
        self.assertEqual(err, "")
        self.assertEqual(
            out,
            "Enter sequence to search for.\n"
            "Found 1 results.\n"
            "Positions: 3\n"
        )

    def test_main_multiple_results(self):
        out, err = self.run_main_capture("14154151415", "1415")
        self.assertEqual(err, "")
        self.assertEqual(
            out,
            "Enter sequence to search for.\n"
            "Found 2 results.\n"
            "Positions: 0 7\n"
        )

    def test_main_more_than_five_results(self):
        out, err = self.run_main_capture("11111111", "1")
        self.assertEqual(err, "")
        self.assertEqual(
            out,
            "Enter sequence to search for.\n"
            "Found 8 results.\n"
            "Positions: 0 1 2 3 4 ...\n"
        )

    def test_main_invalid_input_logs(self):
        out, err = self.run_main_capture("3.1415926535", "14a")
        self.assertEqual(out, "Enter sequence to search for.\n")
        self.assertNotEqual(err, "")

    def test_main_empty_pattern_logs(self):
        out, err = self.run_main_capture("3.1415926535", "")
        self.assertEqual(out, "Enter sequence to search for.\n")
        self.assertNotEqual(err, "")

    def test_main_keyboard_interrupt_logs(self):
        out, err = self.run_main_capture("3.1415926535", KeyboardInterrupt())
        self.assertEqual(out, "Enter sequence to search for.\n")
        self.assertIn("Interrupted by user.", err)

    def test_main_missing_file_logs(self):
        out_buf = io.StringIO()
        err_buf = io.StringIO()

        with tempfile.TemporaryDirectory() as tmpdir:
            old_cwd = os.getcwd()
            os.chdir(tmpdir)
            try:
                with redirect_stdout(out_buf), redirect_stderr(err_buf):
                    problem4.main()
            finally:
                os.chdir(old_cwd)

        self.assertEqual(out_buf.getvalue(), "")
        self.assertNotEqual(err_buf.getvalue(), "")


if __name__ == "__main__":
    unittest.main()