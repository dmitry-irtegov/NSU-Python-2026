import unittest
from io import StringIO
from unittest.mock import patch

import problem4 as main


class TestPiSearch(unittest.TestCase):

    def run_case(self, seq, expected):
        with patch("builtins.input", return_value=seq), \
             patch("sys.stdout", new=StringIO()) as mock_out:

            main.main()

            self.assertEqual(mock_out.getvalue(), expected)

    def test_example_123(self):
        self.run_case(
            "123",
            "Found 4185 results.\n"
            "Positions: 1923 2937 2975 3891 6547 ...\n"
        )

    def test_example_1415(self):
        self.run_case(
            "1415",
            "Found 424 results.\n"
            "Positions: 0 6954 29135 45233 79686 ...\n"
        )

    def test_no_results(self):
        self.run_case(
            "999999999",
            "Found 0 results.\n"
        )

    def test_single_result(self):
        self.run_case(
            "123456",
            "Found 2 results.\n"
            "Positions: 2458884 3735792 ...\n"
        )

    def test_inccorect_input(self):
        self.run_case(
            "-",
            "Found 0 results.\n"
        )


if __name__ == "__main__":
    unittest.main()