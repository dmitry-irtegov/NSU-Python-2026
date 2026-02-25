import unittest
from dictionary import build_latin_to_english_dict


class TestLatinDictionary(unittest.TestCase):

    def setUp(self):
        self.input_data = [
            "apple - malum, pomum, popula",
            "fruit - baca, bacca, popum",
            "punishment - malum, multa",
        ]

        self.expected = {
            "baca": ["fruit"],
            "bacca": ["fruit"],
            "malum": ["apple", "punishment"],
            "multa": ["punishment"],
            "pomum": ["apple"],
            "popula": ["apple"],
            "popum": ["fruit"],
        }

    def test_full_dictionary(self):
        result = build_latin_to_english_dict(self.input_data)
        self.assertEqual(result, self.expected)

    def test_key_exists(self):
        result = build_latin_to_english_dict(self.input_data)
        self.assertIn("malum", result)

    def test_value_correct(self):
        result = build_latin_to_english_dict(self.input_data)
        self.assertListEqual(result["malum"], ["apple", "punishment"])


if __name__ == "__main__":
    unittest.main()