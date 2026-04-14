#!/usr/bin/env python3

import unittest
from tempfile import NamedTemporaryFile

from main import make_latin_dict


class TestCumulativeSums(unittest.TestCase):
    def setUp(self):
        self.temp_file = NamedTemporaryFile()

    def tearDown(self):
        self.temp_file.close()

    def write_dict_to_file(self, content):
        with open(self.temp_file.name, 'w') as f:
            f.write(content)

    def test_empty(self):
        self.write_dict_to_file("")
        self.assertEqual(make_latin_dict(self.temp_file.name), {})

    def test_empty_lines(self):
        self.write_dict_to_file('''

            apple - malum

            fruit - baca

        ''')
        self.assertEqual(make_latin_dict(self.temp_file.name), {
            "malum": ["apple"],
            "baca": ["fruit"],
        })

    def test_example(self):
        self.write_dict_to_file('''
            apple - malum, pomum, popula
            fruit - baca, bacca, popum
            punishment - malum, multa
        ''')
        self.assertEqual(make_latin_dict(self.temp_file.name), {
            "baca": ["fruit"],
            "bacca": ["fruit"],
            "malum": ["apple", "punishment"],
            "multa": ["punishment"],
            "pomum": ["apple"],
            "popula": ["apple"],
            "popum": ["fruit"]
        })


if __name__ == "__main__":
    unittest.main()
