import unittest

from problem2_4 import find_all

PI_DIGITS = "14159265358979323846264338327950288"


class TestFindAll(unittest.TestCase):

    def test_single_occurrence(self):
        self.assertEqual(find_all(PI_DIGITS, "9265"), [4])

    def test_multiple_occurrences(self):
        positions = find_all(PI_DIGITS, "32")
        self.assertEqual(positions, [i for i in range(len(PI_DIGITS) - 1)
                                     if PI_DIGITS[i:i+2] == "32"])

    def test_overlapping_occurrences(self):
        positions = find_all(PI_DIGITS, "33")
        for pos in positions:
            self.assertEqual(PI_DIGITS[pos:pos+2], "33")

    def test_no_occurrence(self):
        self.assertEqual(find_all(PI_DIGITS, "0000"), [])

    def test_empty_substring(self):
        self.assertIsInstance(find_all(PI_DIGITS, ""), list)

    def test_substring_equals_text(self):
        self.assertEqual(find_all(PI_DIGITS, PI_DIGITS), [0])

    def test_substring_longer_than_text(self):
        self.assertEqual(find_all(PI_DIGITS, PI_DIGITS + "0"), [])

    def test_single_digit_search(self):
        positions = find_all(PI_DIGITS, "1")
        self.assertEqual(len(positions), PI_DIGITS.count("1"))

    def test_returns_list(self):
        self.assertIsInstance(find_all(PI_DIGITS, "14"), list)


if __name__ == "__main__":
    unittest.main()