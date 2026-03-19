import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch

from problem1 import Timer


class TestTimer(unittest.TestCase):
    def test_prints_elapsed_time(self):
        with patch("problem1.time.perf_counter", side_effect=[0.0, 2.5]):
            buf = io.StringIO()
            with redirect_stdout(buf):
                with Timer() as timer:
                    pass

        output = buf.getvalue().strip()
        self.assertEqual(output, "Time elapsed: 2.5 s")
        self.assertEqual(timer.get_value(), 2.5)

    def test_returns_current_value_inside_block(self):
        with patch("problem1.time.perf_counter", side_effect=[10.0, 10.4, 12.0]):
            buf = io.StringIO()
            with redirect_stdout(buf):
                with Timer() as timer:
                    self.assertAlmostEqual(timer.get_value(), 0.4)

            self.assertEqual(timer.get_value(), 2.0)

    def test_does_not_suppress_exceptions(self):
        with patch("problem1.time.perf_counter", side_effect=[1.0, 2.0]):
            buf = io.StringIO()
            with redirect_stdout(buf):
                with self.assertRaises(RuntimeError):
                    with Timer() as timer:
                        raise RuntimeError("Error")

        output = buf.getvalue().strip()
        self.assertEqual(output, "Time elapsed: 1.0 s")
        self.assertEqual(timer.get_value(), 1.0)


if __name__ == "__main__":
    unittest.main()
