#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random
import unittest
from functools import partial
from itertools import groupby

from problem1 import (
    random_middle,
    sort_middle,
    transform_text,
    transform_word,
)


def make_random_middle(seed):
    return partial(random_middle, rng=random.Random(seed))


def make_random_text(seed, word_count):
    rng = random.Random(seed)
    english_word_chars = "abcdefghijklmnopqrstuvwxyz"
    russian_word_chars = "абвгдежзийклмнопрстуфхцчшщыэюя"
    chinese_word_chars = "中华人民共和国"
    word_chars = english_word_chars + russian_word_chars + chinese_word_chars
    separator_chars = " ,.!?;:\n\t0123456789-_"
    parts = []

    for _ in range(word_count):
        parts.append("".join(rng.choice(word_chars) for _ in range(rng.randint(1, 14))))
        parts.append(
            "".join(rng.choice(separator_chars) for _ in range(rng.randint(1, 5)))
        )

    return "".join(parts)


def split_text(text):
    return [
        (is_word, "".join(chars)) for is_word, chars in groupby(text, key=str.isalpha)
    ]


class TestTransformWord(unittest.TestCase):
    def test_short_words_stay_unchanged(self):
        self.assertEqual(transform_word("a", sort_middle), "a")
        self.assertEqual(transform_word("to", sort_middle), "to")
        self.assertEqual(transform_word("cat", sort_middle), "cat")

    def test_sort_mode_sorts_english_inner_letters(self):
        self.assertEqual(transform_word("zdcba", sort_middle), "zbcda")

    def test_sort_mode_sorts_russian_inner_letters(self):
        self.assertEqual(transform_word("привет", sort_middle), "пвеирт")

    def test_sort_mode_sorts_inner_letters_case_insensitively(self):
        self.assertEqual(transform_word("xBay", sort_middle), "xaBy")

    def test_random_mode_is_reproducible_for_seeded_generator(self):
        seed = 73
        word = "abcdef"
        transform_middle = make_random_middle(seed)

        first = transform_word(word, transform_middle)
        second = transform_word(word, make_random_middle(seed))

        self.assertEqual(first, second)
        self.assertEqual(first[0], word[0])
        self.assertEqual(first[-1], word[-1])
        self.assertEqual(sorted(first[1:-1]), sorted(word[1:-1]))

    def test_random_mode_preserves_word_edges_and_inner_letters(self):
        transform_middle = make_random_middle(91)
        word = "encyclopedia"

        result = transform_word(word, transform_middle)

        self.assertEqual(result[0], word[0])
        self.assertEqual(result[-1], word[-1])
        self.assertEqual(sorted(result[1:-1]), sorted(word[1:-1]))

    def test_random_mode_can_change_inner_letter_order(self):
        word = "abcdefghijklmnopqrstuvwxyz"

        result = transform_word(word, make_random_middle(73))

        self.assertNotEqual(result, word)


class TestTransformText(unittest.TestCase):
    def test_empty_text_stays_unchanged(self):
        self.assertEqual(transform_text("", sort_middle), "")

    def test_text_without_words_stays_unchanged(self):
        text = "123, -_!?\n"

        self.assertEqual(transform_text(text, sort_middle), text)

    def test_four_letter_word_is_transformed(self):
        self.assertEqual(transform_text("dcba", sort_middle), "dbca")

    def test_text_can_start_with_separator(self):
        self.assertEqual(transform_text(", zdcba", sort_middle), ", zbcda")

    def test_uses_passed_transform_function(self):
        result = transform_text("abcd, efgh!", str.upper)

        self.assertEqual(result, "aBCd, eFGh!")

    def test_preserves_punctuation_spaces_and_digits(self):
        text = "Hi, zdcba 123!"
        expected = "Hi, zbcda 123!"

        self.assertEqual(transform_text(text, sort_middle), expected)

    def test_transforms_russian_english_and_chinese_words(self):
        text = "привет world 中华人民共和国"
        expected = "пвеирт wlord 中人共华和民国"

        self.assertEqual(transform_text(text, sort_middle), expected)


class TestLargeRandomText(unittest.TestCase):
    def assert_common_text_rules(self, original, result):
        self.assertEqual(len(result), len(original))

        original_parts = split_text(original)
        result_parts = split_text(result)
        self.assertEqual(len(result_parts), len(original_parts))

        for original_part, result_part in zip(original_parts, result_parts):
            original_is_word, original_text = original_part
            result_is_word, result_text = result_part

            self.assertEqual(result_is_word, original_is_word)
            if not original_is_word or len(original_text) <= 3:
                self.assertEqual(result_text, original_text)
                continue

            self.assertEqual(result_text[0], original_text[0])
            self.assertEqual(result_text[-1], original_text[-1])
            self.assertEqual(sorted(result_text[1:-1]), sorted(original_text[1:-1]))

    def test_sort_mode_handles_large_random_text(self):
        text = make_random_text(105, 1000)

        result = transform_text(text, sort_middle)

        self.assert_common_text_rules(text, result)
        for original_part, result_part in zip(split_text(text), split_text(result)):
            is_word, original_text = original_part
            result_text = result_part[1]

            if is_word and len(original_text) > 3:
                expected_middle = "".join(sorted(original_text[1:-1], key=str.casefold))
                self.assertEqual(result_text[1:-1], expected_middle)

    def test_random_mode_handles_large_random_text(self):
        text = make_random_text(206, 1000)
        transform_middle = make_random_middle(307)

        result = transform_text(text, transform_middle)

        self.assert_common_text_rules(text, result)

    def test_random_mode_is_reproducible_on_large_random_text(self):
        seed = 509
        text = make_random_text(408, 1000)

        first = transform_text(text, make_random_middle(seed))
        second = transform_text(text, make_random_middle(seed))

        self.assertEqual(first, second)


if __name__ == "__main__":
    unittest.main()
