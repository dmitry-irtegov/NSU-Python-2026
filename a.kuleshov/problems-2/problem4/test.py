import unittest
from problem4 import find_sequence_positions

class TestFindSequencePositions(unittest.TestCase):

    def test_single_match(self):
        pi_digits = "1415926535"
        sequence = "1415"

        result = find_sequence_positions(pi_digits, sequence)

        self.assertEqual(result, [0])

    def test_multiple_matches(self):
        pi_digits = "123123123"
        sequence = "123"

        result = find_sequence_positions(pi_digits, sequence)

        self.assertEqual(result, [0, 3, 6])

    def test_overlapping_matches(self):
        pi_digits = "11111"
        sequence = "11"

        result = find_sequence_positions(pi_digits, sequence)

        self.assertEqual(result, [0, 1, 2, 3])

    def test_no_matches(self):
        pi_digits = "31415926"
        sequence = "999"

        result = find_sequence_positions(pi_digits, sequence)

        self.assertEqual(result, [])

    def test_match_in_middle(self):
        pi_digits = "987654321"
        sequence = "654"

        result = find_sequence_positions(pi_digits, sequence)

        self.assertEqual(result, [3])

if __name__ == "__main__":
    unittest.main()