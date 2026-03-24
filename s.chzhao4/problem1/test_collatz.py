import unittest
from problem3 import collatz_conjecture

class TestCollatzConjecture(unittest.TestCase):

    def test_valid_positive_integers(self):
        expected_3 = ['3', '10', '5', '16', '8', '4', '2', '1']
        self.assertEqual(collatz_conjecture(3), expected_3)

        self.assertEqual(collatz_conjecture(1), ['1'])

    def test_zero_and_negative_integers(self):
        with self.assertRaises(ValueError):
            collatz_conjecture(0)

        with self.assertRaises(ValueError):
            collatz_conjecture(-5)


if __name__ == '__main__':
    unittest.main()