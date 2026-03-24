import unittest
from problem4 import generate_ten_green_bottles

class TestGreenBottles(unittest.TestCase):

    def setUp(self):
        self.lyrics = generate_ten_green_bottles()

    def test_total_lines(self):
        self.assertEqual(len(self.lyrics), 40)

    def test_first_verse(self):
        expected_first_verse = [
            "Ten green bottles hanging on the wall,",
            "Ten green bottles hanging on the wall,",
            "And if one green bottle should accidentally fall,",
            "There'll be nine green bottles hanging on the wall."
        ]
        self.assertEqual(self.lyrics[0:4], expected_first_verse)

    def test_transition_verse(self):
        expected_verse = [
            "Two green bottles hanging on the wall,",
            "Two green bottles hanging on the wall,",
            "And if one green bottle should accidentally fall,",
            "There'll be one green bottle hanging on the wall."
        ]
        self.assertEqual(self.lyrics[-8:-4], expected_verse)

    def test_last_verse(self):
        expected_last_verse = [
            "One green bottle hanging on the wall,",
            "One green bottle hanging on the wall,",
            "If that one green bottle should accidentally fall,",
            "There'll be no green bottles hanging on the wall."
        ]
        self.assertEqual(self.lyrics[-4:], expected_last_verse)

if __name__ == '__main__':
    unittest.main()