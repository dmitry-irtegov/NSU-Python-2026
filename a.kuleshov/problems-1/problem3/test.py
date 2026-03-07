import unittest
from problem3 import collatz_sequence

class TestCollatzSequence(unittest.TestCase):

    def test_start_and_end(self):
        seq = collatz_sequence(7)
        self.assertEqual(seq[0], 7)
        self.assertEqual(seq[-1], 1)

    def test_known_sequence_for_3(self):
        self.assertEqual(
            collatz_sequence(3),
            [3, 10, 5, 16, 8, 4, 2, 1]
        )

    def test_sequence_length_for_9(self):
        seq = collatz_sequence(9)
        self.assertEqual(len(seq), 20)

    def test_power_of_two(self):
        seq = collatz_sequence(16)
        self.assertEqual(seq, [16, 8, 4, 2, 1])

    def test_all_numbers_positive(self):
        seq = collatz_sequence(27)
        self.assertTrue(all(x > 0 for x in seq))

    def test_reaches_one(self):
        seq = collatz_sequence(1347)
        self.assertEqual(seq[-1], 1)

if __name__ == "__main__":
    unittest.main()