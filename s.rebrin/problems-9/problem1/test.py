import unittest
from io import StringIO
import sys
from unittest.mock import patch

from main import Timer


class TestTimer(unittest.TestCase):
    def test_prints_output(self):
        captured = StringIO()
        sys.stdout = captured

        with Timer():
            pass

        sys.stdout = sys.__stdout__

        output = captured.getvalue()
        self.assertIn("Elapsed time:", output)

    def test_prints_with_name(self):
        captured = StringIO()
        sys.stdout = captured

        with Timer("test"):
            pass

        sys.stdout = sys.__stdout__

        output = captured.getvalue()
        self.assertIn("[test]", output)
        self.assertIn("Elapsed time:", output)

    def test_elapsed_attribute_exists(self):
        with Timer() as t:
            pass

        self.assertTrue(hasattr(t, "elapsed"))
        self.assertGreaterEqual(t.elapsed, 0)

    def test_exact_time_with_mock(self):
        with patch("time.perf_counter", side_effect=[1.0, 2.5]):
            captured = StringIO()
            sys.stdout = captured

            with Timer() as t:
                pass

            sys.stdout = sys.__stdout__

            self.assertAlmostEqual(t.elapsed, 1.5, places=6)

            output = captured.getvalue()
            self.assertIn("1.500000", output)

    def test_exception_does_not_break(self):
        captured = StringIO()
        sys.stdout = captured

        try:
            with Timer():
                raise ValueError("error")
        except ValueError:
            pass

        sys.stdout = sys.__stdout__

        output = captured.getvalue()
        self.assertIn("Elapsed time:", output)


if __name__ == "__main__":
    unittest.main()
