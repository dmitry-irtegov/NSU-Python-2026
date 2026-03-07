import io
import random
import unittest
from contextlib import redirect_stderr, redirect_stdout
from unittest.mock import patch

import problem2


class TestClampSequence(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(problem2.clamp_sequence([1, 5, 10], 3, 7), [3, 5, 7])

    def test_all_inside(self):
        self.assertEqual(problem2.clamp_sequence([3, 4, 5], 3, 7), [3, 4, 5])

    def test_empty_seq(self):
        self.assertEqual(problem2.clamp_sequence([], 0, 1), [])

    def test_invalid_range_returns_empty_and_logs(self):
        err = io.StringIO()
        with redirect_stderr(err):
            self.assertEqual(problem2.clamp_sequence([1, 2, 3], 10, 0), [])
        self.assertNotEqual(err.getvalue(), "")

    def test_invariants_random(self):
        rng = random.Random(2026)
        for _ in range(200):
            a = rng.randint(-50, 50)
            b = rng.randint(a, a + 100)
            seq = [rng.randint(-200, 200) for _ in range(rng.randint(0, 200))]
            res = problem2.clamp_sequence(seq, a, b)

            self.assertEqual(len(res), len(seq))
            for x, y in zip(seq, res):
                self.assertGreaterEqual(y, a)
                self.assertLessEqual(y, b)
                if x < a:
                    self.assertEqual(y, a)
                elif x > b:
                    self.assertEqual(y, b)
                else:
                    self.assertEqual(y, x)


class TestMainIO(unittest.TestCase):
    def run_main_capture(self, inputs):
        out_buf = io.StringIO()
        err_buf = io.StringIO()

        def side_effect():
            return inputs.pop(0)

        with patch("builtins.input", side_effect=side_effect), redirect_stdout(out_buf), redirect_stderr(err_buf):
            problem2.main()

        return out_buf.getvalue(), err_buf.getvalue()

    def test_main_ok(self):
        out, err = self.run_main_capture(["1 5 10", "3 7"])
        self.assertEqual(out, "[3, 5, 7]\n")
        self.assertEqual(err, "")

    def test_main_whitespace_ok(self):
        out, err = self.run_main_capture(["  1   5   10  ", "   3    7  "])
        self.assertEqual(out, "[3, 5, 7]\n")
        self.assertEqual(err, "")

    def test_main_invalid_bounds_count(self):
        out, err = self.run_main_capture(["1 2 3", "10"])
        self.assertEqual(out, "")
        self.assertNotEqual(err, "")

    def test_main_non_int_in_seq(self):
        out, err = self.run_main_capture(["1 a 3", "0 10"])
        self.assertEqual(out, "")
        self.assertNotEqual(err, "")

    def test_main_invalid_range(self):
        out, err = self.run_main_capture(["1 2 3", "10 0"])
        self.assertEqual(out, "")
        self.assertNotEqual(err, "")

    def test_stderr_never_pollutes_stdout_on_errors(self):
        cases = [
            ["1 2 3", ""],
            ["1 2 3", "x y"],
            ["1 x 3", "0 1"],
            ["1 2 3", "5 2"],
            ["", ""],
            ["", "x y"],
        ]
        for inp in cases:
            out, err = self.run_main_capture(inp[:])
            self.assertEqual(out, "")
            self.assertNotEqual(err, "")

    def test_empty_sequence_is_allowed(self):
        out, err = self.run_main_capture(["", "0 1"])
        self.assertEqual(out, "[]\n")
        self.assertEqual(err, "")


if __name__ == "__main__":
    unittest.main()
