import unittest
from unittest.mock import patch
import io
from problem3 import print_collatz_seq


def get_output(number, maxIter=1 << 61):
    with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
        print_collatz_seq(number, maxIter)
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


class TestCollatzSeqMaxIter(unittest.TestCase):
    def test_exceeds_max_iter(self):
        self.assertEqual(get_output(3, maxIter=3), '[]')

    def test_exceeds_max_iter_single(self):
        self.assertEqual(get_output(3, maxIter=1), '[]')

    def test_exact_max_iter_completes(self):
        self.assertEqual(get_output(2, maxIter=1), '2 -> 1')

    def test_default_max_iter_large_number(self):
        output = get_output(1_000_000)
        self.assertTrue(output.endswith('-> 1'))


if __name__ == '__main__':
    unittest.main()