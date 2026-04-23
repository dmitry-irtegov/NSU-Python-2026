#!/usr/bin/env python3

import unittest
from io import StringIO
from unittest.mock import patch

from main import collatz_sequence


class TestCumulativeSums(unittest.TestCase):
    def check(self, start, expected):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            collatz_sequence(start)
            self.assertEqual(mock_stdout.getvalue(), expected)

    def test_example(self):
        self.check(3, "3 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1")

    def test_even(self):
        self.check(68, "68 -> 34 -> 17 -> 52 -> 26 -> 13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1")

    def test_odd(self):
        self.check(69, "69 -> 208 -> 104 -> 52 -> 26 -> 13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1")


if __name__ == "__main__":
    unittest.main()
