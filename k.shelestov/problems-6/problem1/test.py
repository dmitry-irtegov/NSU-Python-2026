import unittest
import re
import random

from problem1 import process_text


TEXT = """Существует исследование, говорящее о том, что в словах текста можно произвольно переставить буквы (не затрагивая первую и последнюю), и от этого читабельность текста практически не ухудшится. Напишите программу для проверки этого факта. Ваша программа
должна получать на вход какой-нибудь текст и переставлять буквы в его словах случайным образом. Также у программы должен быть режим, в котором буквы переставляются не
случайным образом, а сортируются по алфавиту. Сравните результаты."""


def check_word_structure(original: str, result: str):
    orig_tokens = re.findall(r"\w+|[^\w]+", original)
    res_tokens = re.findall(r"\w+|[^\w]+", result)

    for o, r in zip(orig_tokens, res_tokens):
        if o.isalpha():
            if len(o) > 1:
                assert o[0] == r[0], f"First letter changed: {o} -> {r}"
                assert o[-1] == r[-1], f"Last letter changed: {o} -> {r}"
        else:
            assert o == r, f"Punctuation changed: {o} -> {r}"


def check_sorted_inner_letters(original: str, result: str):
    orig_tokens = re.findall(r"\w+|[^\w]+", original)
    res_tokens = re.findall(r"\w+|[^\w]+", result)

    for o, r in zip(orig_tokens, res_tokens):
        if o.isalpha() and len(o) > 2:
            assert list(r[1:-1]) == sorted(o[1:-1]), f"Not sorted: {o} -> {r}"


class TestTextProcessing(unittest.TestCase):

    def test_structure_random_big_text(self):
        rng = random.Random(42)
        result = process_text(TEXT, mode="random", rng=rng)
        check_word_structure(TEXT, result)

    def test_structure_sort_big_text(self):
        rng = random.Random(42)
        result = process_text(TEXT, mode="sort", rng=rng)

        check_word_structure(TEXT, result)
        check_sorted_inner_letters(TEXT, result)

    def test_determinism_random(self):
        rng1 = random.Random(42)
        rng2 = random.Random(42)

        r1 = process_text(TEXT, "random", rng1)
        r2 = process_text(TEXT, "random", rng2)

        self.assertEqual(r1, r2)


if __name__ == "__main__":
    unittest.main()