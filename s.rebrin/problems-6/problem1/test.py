import unittest
import re
from main import randomize_words


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
            original_middle = list(o[1:-1])
            result_middle = list(r[1:-1])

            assert result_middle == sorted(original_middle), f"Not sorted: {o} -> {r}"


class TestRandomizeWords(unittest.TestCase):
    def test_structure_random(self):
        text = "hello, world!!! amazing test?"
        result = randomize_words(text, seed=42, mode="random")
        check_word_structure(text, result)

    def test_structure_sort(self):
        text = "hello, world!!! amazing test?"
        result = randomize_words(text, seed=42, mode="sort")
        check_word_structure(text, result)
        check_sorted_inner_letters(text, result)

    def test_unicode_random(self):
        text = """Существует исследование, говорящее о том, что в словах текста можно произвольно переставить буквы (не затрагивая первую и последнюю), и от этого читабельность текста практически не ухудшится. Напишите программу для проверки этого факта. Ваша программа
должна получать на вход какой-нибудь текст и переставлять буквы в его словах случайным образом. Также у программы должен быть режим, в котором буквы переставляются не
случайным образом, а сортируются по алфавиту. Сравните результаты."""
        result = randomize_words(text, seed=42, mode="random")
        check_word_structure(text, result)

    def test_unicode_sort(self):
        text = """Существует исследование, говорящее о том, что в словах текста можно произвольно переставить буквы (не затрагивая первую и последнюю), и от этого читабельность текста практически не ухудшится. Напишите программу для проверки этого факта. Ваша программа
должна получать на вход какой-нибудь текст и переставлять буквы в его словах случайным образом. Также у программы должен быть режим, в котором буквы переставляются не
случайным образом, а сортируются по алфавиту. Сравните результаты."""
        result = randomize_words(text, mode="sort")
        check_word_structure(text, result)
        check_sorted_inner_letters(text, result)


if __name__ == "__main__":
    unittest.main()
