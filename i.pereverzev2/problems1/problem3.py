#!/usr/bin/python
import unittest
import sys
from io import StringIO


def collatc(num):
    print(num, end="")
    while num != 1:
        if num % 2 == 0:
            num //= 2
        else:
            num = num * 3 + 1
        print(" -> ", num, end="")


class TestCollatc(unittest.TestCase):

    def test_output(self):
        original_stdout = sys.stdout
        sys.stdout = StringIO()

        collatc(5)

        output = sys.stdout.getvalue()
        sys.stdout = original_stdout

        expected = "5 ->  16 ->  8 ->  4 ->  2 ->  1"
        self.assertEqual(output, expected)

    def test_one(self):
        original_stdout = sys.stdout
        sys.stdout = StringIO()

        collatc(1)

        output = sys.stdout.getvalue()
        sys.stdout = original_stdout

        self.assertEqual(output, "1")


if __name__ == "__main__":
    unittest.main()
