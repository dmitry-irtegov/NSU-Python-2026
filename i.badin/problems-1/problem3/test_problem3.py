from collections.abc import Iterator
from io import StringIO
from unittest.mock import patch
from itertools import islice
import unittest

from problem3 import collatz_sequence, main


class CollatzTests(unittest.TestCase):
    def test_sequence_for_three(self) -> None:
        self.assertEqual(list(collatz_sequence(3)), [3, 10, 5, 16, 8, 4, 2, 1])

    def test_sequence_for_one(self) -> None:
        self.assertEqual(list(collatz_sequence(1)), [1])

    def test_long_sequence_for_twenty_seven(self) -> None:
        sequence: list[int] = list(collatz_sequence(27))

        self.assertEqual(len(sequence), 112)
        self.assertEqual(sequence[:8], [27, 82, 41, 124, 62, 31, 94, 47])
        self.assertEqual(sequence[-8:], [20, 10, 5, 16, 8, 4, 2, 1])

    def test_sequence_can_be_consumed_lazily(self) -> None:
        sequence: Iterator[int] = collatz_sequence(27)

        self.assertIs(sequence, iter(sequence))
        self.assertEqual(list(islice(sequence, 5)), [27, 82, 41, 124, 62])
        self.assertEqual(next(sequence), 31)

    def test_non_positive_input_raises(self) -> None:
        with self.assertRaises(ValueError):
            collatz_sequence(0)

    def test_main_prints_chain_and_result(self) -> None:
        with (
            patch("builtins.input", return_value="3"),
            patch("sys.stdout", new_callable=StringIO) as output,
            patch("sys.stderr", new_callable=StringIO) as errors,
        ):
            main()

        self.assertEqual(output.getvalue(), "3 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1\n")
        self.assertEqual(errors.getvalue(), "")

    def test_main_reports_conversion_error_to_stderr(self) -> None:
        with (
            patch("builtins.input", return_value="abc"),
            patch("sys.stdout", new_callable=StringIO) as output,
            patch("sys.stderr", new_callable=StringIO) as errors,
        ):
            main()

        self.assertEqual(output.getvalue(), "")
        self.assertEqual(errors.getvalue(), "Input error: expected integer\n")


if __name__ == "__main__":
    unittest.main()
