import unittest
from unittest.mock import patch
import io
from problem3 import print_collatz_seq


def get_output(number):
    with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
        print_collatz_seq(number)
        return mock_stdout.getvalue().strip()


class TestCollatzSeqKnownValues(unittest.TestCase):
    def test_number_1(self):
        self.assertEqual(get_output(1), '1')

    def test_number_2(self):
        self.assertEqual(get_output(2), '2 -> 1')

    def test_number_3(self):
        self.assertEqual(get_output(3), '3 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1')

    def test_number_6(self):
        self.assertEqual(get_output(6), '6 -> 3 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1')

    def test_number_27_length(self):
        output = get_output(27)
        self.assertEqual(len(output.split(' -> ')), 112)


if __name__ == '__main__':
    unittest.main()