import io
import re
import unittest
from contextlib import redirect_stderr, redirect_stdout
from unittest.mock import patch

import problem4


class TestGenerateSong(unittest.TestCase):
    def test_first_and_last_lines_for_10(self):
        song = problem4.generate_ten_green_bottles(10)
        lines = song.strip().split("\n")
        self.assertEqual(lines[0], "Ten green bottles hanging on the wall,")
        self.assertEqual(lines[1], "Ten green bottles hanging on the wall,")
        self.assertEqual(lines[-2], "If that one green bottle should accidentally fall")
        self.assertEqual(lines[-1], "There’ll be no green bottles hanging on the wall.")

    def test_start_1_exact(self):
        song = problem4.generate_ten_green_bottles(1)
        lines = song.strip().split("\n")
        self.assertEqual(lines, [
            "One green bottle hanging on the wall,",
            "One green bottle hanging on the wall,",
            "If that one green bottle should accidentally fall",
            "There’ll be no green bottles hanging on the wall.",
        ])

    def test_structure_and_grammar(self):
        song = problem4.generate_ten_green_bottles(10)
        lines = song.strip().split("\n")
        self.assertEqual(len(lines), 40)

        for i in range(10):
            n = 10 - i
            base = i * 4
            cur = problem4.number_to_words(n).capitalize()
            cur_b = "bottle" if n == 1 else "bottles"

            self.assertEqual(lines[base], f"{cur} green {cur_b} hanging on the wall,")
            self.assertEqual(lines[base + 1], f"{cur} green {cur_b} hanging on the wall,")

            if n == 1:
                self.assertEqual(lines[base + 2], "If that one green bottle should accidentally fall")
                self.assertEqual(lines[base + 3], "There’ll be no green bottles hanging on the wall.")
            else:
                nxt = n - 1
                nxt_w = problem4.number_to_words(nxt)
                nxt_b = "bottle" if nxt == 1 else "bottles"
                self.assertEqual(lines[base + 2], "And if one green bottle should accidentally fall,")
                self.assertEqual(lines[base + 3], f"There’ll be {nxt_w} green {nxt_b} hanging on the wall.")

    def test_full_output_for_10_exact(self):
        expected = (
            "Ten green bottles hanging on the wall,\n"
            "Ten green bottles hanging on the wall,\n"
            "And if one green bottle should accidentally fall,\n"
            "There’ll be nine green bottles hanging on the wall.\n"
            "Nine green bottles hanging on the wall,\n"
            "Nine green bottles hanging on the wall,\n"
            "And if one green bottle should accidentally fall,\n"
            "There’ll be eight green bottles hanging on the wall.\n"
            "Eight green bottles hanging on the wall,\n"
            "Eight green bottles hanging on the wall,\n"
            "And if one green bottle should accidentally fall,\n"
            "There’ll be seven green bottles hanging on the wall.\n"
            "Seven green bottles hanging on the wall,\n"
            "Seven green bottles hanging on the wall,\n"
            "And if one green bottle should accidentally fall,\n"
            "There’ll be six green bottles hanging on the wall.\n"
            "Six green bottles hanging on the wall,\n"
            "Six green bottles hanging on the wall,\n"
            "And if one green bottle should accidentally fall,\n"
            "There’ll be five green bottles hanging on the wall.\n"
            "Five green bottles hanging on the wall,\n"
            "Five green bottles hanging on the wall,\n"
            "And if one green bottle should accidentally fall,\n"
            "There’ll be four green bottles hanging on the wall.\n"
            "Four green bottles hanging on the wall,\n"
            "Four green bottles hanging on the wall,\n"
            "And if one green bottle should accidentally fall,\n"
            "There’ll be three green bottles hanging on the wall.\n"
            "Three green bottles hanging on the wall,\n"
            "Three green bottles hanging on the wall,\n"
            "And if one green bottle should accidentally fall,\n"
            "There’ll be two green bottles hanging on the wall.\n"
            "Two green bottles hanging on the wall,\n"
            "Two green bottles hanging on the wall,\n"
            "And if one green bottle should accidentally fall,\n"
            "There’ll be one green bottle hanging on the wall.\n"
            "One green bottle hanging on the wall,\n"
            "One green bottle hanging on the wall,\n"
            "If that one green bottle should accidentally fall\n"
            "There’ll be no green bottles hanging on the wall.\n"
        )
        self.assertEqual(problem4.generate_ten_green_bottles(10), expected)

    def test_invalid_start_logs_and_returns_empty(self):
        err = io.StringIO()
        with redirect_stderr(err):
            song = problem4.generate_ten_green_bottles(0)
        self.assertEqual(song, "")
        self.assertNotEqual(err.getvalue(), "")

    def test_numbers_only_from_0_to_10_if_any(self):
        song = problem4.generate_ten_green_bottles(10)
        nums = [int(x) for x in re.findall(r"\b\d+\b", song)]
        self.assertTrue(all(0 <= x <= 10 for x in nums))


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
            problem4.main()

        return out_buf.getvalue(), err_buf.getvalue()

    def test_main_empty_input_defaults_to_10(self):
        out, err = self.run_main_capture("")
        self.assertEqual(err, "")
        self.assertTrue(out.startswith("Ten green bottles hanging on the wall,"))

    def test_main_custom_start(self):
        out, err = self.run_main_capture("3")
        self.assertEqual(err, "")
        self.assertTrue(out.startswith("Three green bottles hanging on the wall,"))
        self.assertTrue(out.strip().endswith("There’ll be no green bottles hanging on the wall."))

    def test_main_invalid_input_logs(self):
        out, err = self.run_main_capture("abc")
        self.assertEqual(out, "")
        self.assertNotEqual(err, "")

    def test_main_invalid_start_logs(self):
        out, err = self.run_main_capture("0")
        self.assertEqual(out, "")
        self.assertNotEqual(err, "")

    def test_main_keyboard_interrupt_logs(self):
        out, err = self.run_main_capture(KeyboardInterrupt())
        self.assertEqual(out, "")
        self.assertNotEqual(err, "")


if __name__ == "__main__":
    unittest.main()