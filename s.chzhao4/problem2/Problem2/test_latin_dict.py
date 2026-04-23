import unittest
from problem2 import invert_dictionary


class TestLatinDictionary(unittest.TestCase):

    def test_image_example(self):
        input_lines = [
            "apple - malum, pomum, popula",
            "fruit - baca, bacca, popum",
            "punishment - malum, multa"
        ]

        expected_output = [
            "baca - fruit",
            "bacca - fruit",
            "malum - apple, punishment",
            "multa - punishment",
            "pomum - apple",
            "popula - apple",
            "popum - fruit"
        ]

        self.assertEqual(invert_dictionary(input_lines), expected_output)

    def test_empty_input(self):
        self.assertEqual(invert_dictionary([]), [])

    def test_ignore_invalid_lines(self):
        input_lines = [
            "apple - malum",
            "this is an invalid line",
            "fruit - baca"
        ]
        expected_output = [
            "baca - fruit",
            "malum - apple"
        ]
        self.assertEqual(invert_dictionary(input_lines), expected_output)

    def test_sorting_english_words(self):
        input_lines = [
            "zebra - testword",
            "apple - testword"
        ]
        expected_output = [
            "testword - apple, zebra"
        ]
        self.assertEqual(invert_dictionary(input_lines), expected_output)


if __name__ == '__main__':
    unittest.main()