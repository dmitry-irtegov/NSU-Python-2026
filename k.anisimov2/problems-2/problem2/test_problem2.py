import io
import unittest
from contextlib import redirect_stderr, redirect_stdout
from unittest.mock import patch

import problem2


class TestConvertDictionary(unittest.TestCase):
    def test_example(self):
        lines = [
            "apple - malum, pomum, popula",
            "fruit - baca, bacca, popum",
            "punishment - malum, multa",
        ]
        self.assertEqual(problem2.convert_dictionary(lines), [
            "baca - fruit",
            "bacca - fruit",
            "malum - apple, punishment",
            "multa - punishment",
            "pomum - apple",
            "popula - apple",
            "popum - fruit",
        ])

    def test_big_complex_example(self):
        lines = [
            "apple - malum, pomum, ariena",
            "fruit - baca, bacca, pomum, fructus",
            "punishment - malum, multa, poena",
            "crime - scelus, crimen, malum",
            "book - liber, codex, volumen",
            "letter - epistula, littera, codex",
            "word - verbum, vocabulum, littera",
            "war - bellum, pugna, proelium",
            "battle - pugna, proelium, certamen",
            "peace - pax, otium",
            "rest - otium, quies",
            "school - schola, ludus",
            "game - ludus, iocus, certamen",
        ]
        self.assertEqual(problem2.convert_dictionary(lines), [
            "ariena - apple",
            "baca - fruit",
            "bacca - fruit",
            "bellum - war",
            "certamen - battle, game",
            "codex - book, letter",
            "crimen - crime",
            "epistula - letter",
            "fructus - fruit",
            "iocus - game",
            "liber - book",
            "littera - letter, word",
            "ludus - game, school",
            "malum - apple, crime, punishment",
            "multa - punishment",
            "otium - peace, rest",
            "pax - peace",
            "poena - punishment",
            "pomum - apple, fruit",
            "proelium - battle, war",
            "pugna - battle, war",
            "quies - rest",
            "scelus - crime",
            "schola - school",
            "verbum - word",
            "vocabulum - word",
            "volumen - book",
        ])

    def test_alphabetical_order(self):
        lines = [
            "zebra - beta, alpha",
            "apple - gamma",
        ]
        self.assertEqual(problem2.convert_dictionary(lines), [
            "alpha - zebra",
            "beta - zebra",
            "gamma - apple",
        ])

    def test_multiple_english_words_for_one_latin(self):
        lines = [
            "apple - malum",
            "punishment - malum",
            "evil - malum",
        ]
        self.assertEqual(problem2.convert_dictionary(lines), [
            "malum - apple, evil, punishment",
        ])

    def test_invalid_line_raises_value_error(self):
        with self.assertRaises(ValueError):
            problem2.convert_dictionary(["apple malum, pomum"])

    def test_invalid_type_raises_type_error(self):
        with self.assertRaises(TypeError):
            problem2.convert_dictionary("apple - malum")

    def test_empty_english_word_raises_value_error(self):
        with self.assertRaises(ValueError):
            problem2.convert_dictionary([" - malum"])

    def test_empty_latin_word_raises_value_error(self):
        with self.assertRaises(ValueError):
            problem2.convert_dictionary(["apple - malum, "])


class TestMainIO(unittest.TestCase):
    def run_main_capture(self, inputs):
        out_buf = io.StringIO()
        err_buf = io.StringIO()

        if isinstance(inputs, BaseException):
            side_effect = inputs
        else:
            data = inputs[:]

            def side_effect():
                return data.pop(0)

        with (
            patch("builtins.input", side_effect=side_effect),
            redirect_stdout(out_buf),
            redirect_stderr(err_buf)
        ):
            problem2.main()

        return out_buf.getvalue(), err_buf.getvalue()

    def test_main_ok(self):
        out, err = self.run_main_capture([
            "3",
            "apple - malum, pomum, popula",
            "fruit - baca, bacca, popum",
            "punishment - malum, multa",
        ])
        self.assertEqual(err, "")
        self.assertEqual(out, "\n".join([
            "baca - fruit",
            "bacca - fruit",
            "malum - apple, punishment",
            "multa - punishment",
            "pomum - apple",
            "popula - apple",
            "popum - fruit",
        ]) + "\n")

    def test_main_big_complex_example(self):
        out, err = self.run_main_capture([
            "13",
            "apple - malum, pomum, ariena",
            "fruit - baca, bacca, pomum, fructus",
            "punishment - malum, multa, poena",
            "crime - scelus, crimen, malum",
            "book - liber, codex, volumen",
            "letter - epistula, littera, codex",
            "word - verbum, vocabulum, littera",
            "war - bellum, pugna, proelium",
            "battle - pugna, proelium, certamen",
            "peace - pax, otium",
            "rest - otium, quies",
            "school - schola, ludus",
            "game - ludus, iocus, certamen",
        ])
        self.assertEqual(err, "")
        self.assertEqual(out, "\n".join([
            "ariena - apple",
            "baca - fruit",
            "bacca - fruit",
            "bellum - war",
            "certamen - battle, game",
            "codex - book, letter",
            "crimen - crime",
            "epistula - letter",
            "fructus - fruit",
            "iocus - game",
            "liber - book",
            "littera - letter, word",
            "ludus - game, school",
            "malum - apple, crime, punishment",
            "multa - punishment",
            "otium - peace, rest",
            "pax - peace",
            "poena - punishment",
            "pomum - apple, fruit",
            "proelium - battle, war",
            "pugna - battle, war",
            "quies - rest",
            "scelus - crime",
            "schola - school",
            "verbum - word",
            "vocabulum - word",
            "volumen - book",
        ]) + "\n")

    def test_main_empty_dictionary(self):
        out, err = self.run_main_capture(["0"])
        self.assertEqual(out, "")
        self.assertEqual(err, "")

    def test_main_invalid_n_logs(self):
        out, err = self.run_main_capture(["abc"])
        self.assertEqual(out, "")
        self.assertNotEqual(err, "")

    def test_main_invalid_line_logs(self):
        out, err = self.run_main_capture([
            "1",
            "apple malum, pomum",
        ])
        self.assertEqual(out, "")
        self.assertNotEqual(err, "")

    def test_main_keyboard_interrupt_logs(self):
        out, err = self.run_main_capture(KeyboardInterrupt())
        self.assertEqual(out, "")
        self.assertIn("Interrupted by user.", err)


if __name__ == "__main__":
    unittest.main()