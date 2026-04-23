import unittest
from problem2 import build_dictionary

class TestBuildDictionaryFormat(unittest.TestCase):
    def test_entry_contains_dash(self):
        result = build_dictionary(["apple - banana"])
        self.assertIn("-", result[0])

    def test_key_before_dash(self):
        result = build_dictionary(["apple - banana"])
        key, _ = result[0].split("-", 1)
        self.assertEqual(key, "banana")

    def test_value_after_dash(self):
        result = build_dictionary(["apple - banana"])
        _, value = result[0].split("-", 1)
        self.assertEqual(value, "apple")

    def test_multiple_values_joined_with_comma(self):
        result = build_dictionary(["apple - banana", "pear - banana"])
        entry = next(r for r in result if r.startswith("banana"))
        _, value = entry.split("-", 1)
        self.assertIn(",", value)
        self.assertIn("apple", value)
        self.assertIn("pear", value)

class TestBuildDictionaryMultipleTranslations(unittest.TestCase):
    def test_one_latin_multiple_english(self):
        result = build_dictionary(["apple - banana", "pear - banana"])
        entry = next(r for r in result if r.startswith("banana"))
        _, value = entry.split("-", 1)
        values = [v.strip() for v in value.split(",")]
        self.assertIn("apple", values)
        self.assertIn("pear", values)

    def test_one_english_multiple_latin(self):
        result = build_dictionary(["apple - banana cherry"])
        self.assertEqual(len(result), 2)

    def test_no_duplicate_keys(self):
        result = build_dictionary(["apple - banana", "pear - banana"])
        keys = [r.split("-")[0] for r in result]
        self.assertEqual(len(keys), len(set(keys)))


class TestBuildDictionaryInvalidInput(unittest.TestCase):
    def test_empty_line_raises(self):
        with self.assertRaises(ValueError):
            build_dictionary([""])

    def test_single_word_raises(self):
        with self.assertRaises(ValueError):
            build_dictionary(["apple"])

    def test_error_message(self):
        with self.assertRaises(ValueError) as ctx:
            build_dictionary(["apple"])
        self.assertEqual(str(ctx.exception), "incorrect format of line")

    def test_valid_line_after_invalid_raises(self):
        with self.assertRaises(ValueError):
            build_dictionary(["apple", "pear - banana"])

if __name__ == '__main__':
    unittest.main()
