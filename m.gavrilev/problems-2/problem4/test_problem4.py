#!/usr/bin/env python3

import random
import re
import unittest
from io import StringIO
from unittest.mock import patch

from problem4 import find_pattern, format_positions, search_and_print


class TestFindPattern(unittest.TestCase):
    def test_single_match(self):
        self.assertEqual(list(find_pattern("12345", "23")), [1])

    def test_multiple_matches(self):
        self.assertEqual(list(find_pattern("5612561256", "12")), [2, 6])

    def test_overlapping_matches(self):
        self.assertEqual(list(find_pattern("1111", "11")), [0, 1, 2])

    def test_no_match(self):
        self.assertEqual(list(find_pattern("12345", "99")), [])

    def test_full_string_match(self):
        self.assertEqual(list(find_pattern("123", "123")), [0])

    def test_single_digit(self):
        self.assertEqual(list(find_pattern("10101", "1")), [0, 2, 4])

    def test_empty_pattern_raises(self):
        with self.assertRaises(ValueError):
            list(find_pattern("123", ""))

    def test_none_pattern_raises(self):
        with self.assertRaises(ValueError):
            list(find_pattern("123", None))

    def test_non_digit_pattern_raises(self):
        with self.assertRaises(ValueError):
            list(find_pattern("123", "abc"))

    def test_mixed_pattern_raises(self):
        with self.assertRaises(ValueError):
            list(find_pattern("123", "1a2"))

    def test_empty_text_raises(self):
        with self.assertRaises(ValueError):
            list(find_pattern("", "1"))

    def test_non_digit_text_raises(self):
        with self.assertRaises(ValueError):
            list(find_pattern("abab1212ab", "12"))

    def test_pattern_longer_than_text(self):
        self.assertEqual(list(find_pattern("12", "12345")), [])

    def test_single_char_text(self):
        self.assertEqual(list(find_pattern("5", "5")), [0])

    def test_single_char_text_no_match(self):
        self.assertEqual(list(find_pattern("5", "3")), [])


class TestFormatPositions(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(format_positions([], 0), "Positions: not found")

    def test_single_position(self):
        self.assertEqual(format_positions([42], 1), "Positions: 42")

    def test_two_positions(self):
        self.assertEqual(format_positions([10, 20], 2), "Positions: 10 20")

    def test_four_positions(self):
        result = format_positions([1, 2, 3, 4], 4)
        self.assertEqual(result, "Positions: 1 2 3 4")

    def test_five_positions(self):
        result = format_positions([0, 1, 2, 3, 4], 5)
        self.assertEqual(result, "Positions: 0 1 2 3 4")

    def test_more_than_five_truncated(self):
        result = format_positions([0, 1, 2, 3, 4], 6)
        self.assertEqual(result, "Positions: 0 1 2 3 4 ...")

    def test_many_positions(self):
        result = format_positions([0, 1, 2, 3, 4], 100)
        self.assertEqual(result, "Positions: 0 1 2 3 4 ...")


class TestSearchAndPrint(unittest.TestCase):
    def test_found(self):
        captured = StringIO()
        with patch("sys.stdout", captured):
            search_and_print("1234512345", "23")
        output = captured.getvalue()
        self.assertIn("Found 2", output)
        self.assertIn("Positions: 1 6", output)

    def test_not_found(self):
        captured = StringIO()
        with patch("sys.stdout", captured):
            search_and_print("12345", "99")
        output = captured.getvalue()
        self.assertIn("Found 0", output)
        self.assertIn("not found", output)

    def test_more_than_five_matches_truncated(self):
        captured = StringIO()
        with patch("sys.stdout", captured):
            search_and_print("1010101010101", "1")
        output = captured.getvalue()
        self.assertIn("Found 7", output)
        self.assertIn("...", output)

    def test_invalid_pattern_prints_error(self):
        captured = StringIO()
        with patch("sys.stderr", captured):
            search_and_print("12345", "abc")
        self.assertIn("Error", captured.getvalue())


def random_digits(rng, length):
    return "".join(str(rng.randint(0, 9)) for _ in range(length))


class TestFindPatternRandom(unittest.TestCase):
    NUM_ITERATIONS = 100

    def test_random_pattern_always_found(self):
        rng = random.Random(42)
        for _ in range(self.NUM_ITERATIONS):
            pattern = random_digits(rng, rng.randint(1, 4))
            pos = rng.randint(0, 50)
            padding_left = random_digits(rng, pos)
            padding_right = random_digits(rng, rng.randint(0, 50))
            text = padding_left + pattern + padding_right
            results = list(find_pattern(text, pattern))
            self.assertIn(pos, results)

    def test_random_matches_equal_regex(self):
        rng = random.Random(43)
        for _ in range(self.NUM_ITERATIONS):
            text = random_digits(rng, rng.randint(10, 200))
            pattern = random_digits(rng, rng.randint(1, 3))
            results = list(find_pattern(text, pattern))
            expected = [m.start() for m in re.finditer(f"(?={pattern})", text)]
            self.assertEqual(results, expected)


if __name__ == "__main__":
    unittest.main()
