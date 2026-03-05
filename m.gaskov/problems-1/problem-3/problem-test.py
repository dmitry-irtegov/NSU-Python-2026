import unittest
from io import StringIO
from unittest.mock import patch

from problem import collatz_sequence, main


class TestCollatzSequence(unittest.TestCase):
    def test_sequence_for_1(self):
        self.assertEqual(list(collatz_sequence(1)), [1])

    def test_sequence_for_3(self):
        self.assertEqual(
            list(collatz_sequence(3)),
            [3, 10, 5, 16, 8, 4, 2, 1]
        )

    def test_sequence_for_6(self):
        self.assertEqual(
            list(collatz_sequence(6)),
            [6, 3, 10, 5, 16, 8, 4, 2, 1]
        )

    def test_sequence_for_even_number(self):
        self.assertEqual(
            list(collatz_sequence(8)),
            [8, 4, 2, 1]
        )

    def test_non_int_raises_type_error(self):
        with self.assertRaises(TypeError):
            list(collatz_sequence("3"))

    def test_zero_raises_value_error(self):
        with self.assertRaises(ValueError):
            list(collatz_sequence(0))

    def test_negative_raises_value_error(self):
        with self.assertRaises(ValueError):
            list(collatz_sequence(-5))


class TestMain(unittest.TestCase):
    def test_main_with_3(self):
        with patch("builtins.input", return_value="3"), \
             patch("sys.stdout", new=StringIO()) as mock_out:
            main()
            self.assertEqual(
                mock_out.getvalue(),
                "3 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1\n"
            )

    def test_main_with_spaces(self):
        with patch("builtins.input", return_value="   6   "), \
             patch("sys.stdout", new=StringIO()) as mock_out:
            main()
            self.assertEqual(
                mock_out.getvalue(),
                "6 -> 3 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1\n"
            )

    def test_main_with_invalid_input(self):
        with patch("builtins.input", return_value="abc"):
            with self.assertRaises(ValueError):
                main()

    def test_main_with_zero(self):
        with patch("builtins.input", return_value="0"):
            with self.assertRaises(ValueError):
                main()


if __name__ == "__main__":
    unittest.main()