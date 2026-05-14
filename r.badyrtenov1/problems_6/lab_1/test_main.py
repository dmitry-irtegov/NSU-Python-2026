#!/usr/bin/env python3

import unittest
from unittest.mock import patch

from main import transform_text, transform_word


class TestTextTransform(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(transform_text("", "random"), "")

    def test_short_words_unchanged(self):
        self.assertEqual(transform_text("I am at a zoo.", "random"), "I am at a zoo.")

    def test_sorted_mode(self):
        self.assertEqual(transform_text("azbycxdw", "sorted"), "abcdxyzw")

    def test_punctuation_preserved(self):
        self.assertEqual(transform_text("Hello, world!", "sorted"), "Hello, wlord!")

    def test_random_mode_with_mock_shuffle(self):
        def reverse_list(lst):
            lst.reverse()

        with patch("main.random.shuffle", side_effect=reverse_list):
            self.assertEqual(transform_text("abcdef", "random"), "aedcbf")

    def test_transform_word_invalid_mode(self):
        with self.assertRaises(ValueError):
            transform_word("example", "unknown")


if __name__ == "__main__":
    unittest.main()
