#!/usr/bin/env python3

import unittest
from os import path
from tempfile import TemporaryDirectory

from main import get_sorted_files


class TestSortedFiles(unittest.TestCase):

    def setUp(self):
        self.temp_dir = TemporaryDirectory()

    def tearDown(self):
        self.temp_dir.cleanup()

    def create_file(self, name, content):
        with open(path.join(self.temp_dir.name, name), 'w') as f:
            f.write(content)

    def test_empty_directory(self):
        self.assertEqual(get_sorted_files(self.temp_dir.name), [])

    def test_single_file(self):
        self.create_file("a.txt", "hello")
        self.assertEqual(get_sorted_files(self.temp_dir.name), [("a.txt", 5)])

    def test_sort_by_size(self):
        self.create_file("small.txt", "123")
        self.create_file("big.txt", "123456789")
        self.assertEqual(get_sorted_files(self.temp_dir.name), [("big.txt", 9), ("small.txt", 3)])

    def test_sort_by_name_if_same_size(self):
        self.create_file("b.txt", "12345")
        self.create_file("a.txt", "abcde")
        self.assertEqual(get_sorted_files(self.temp_dir.name), [("a.txt", 5), ("b.txt", 5)])


if __name__ == "__main__":
    unittest.main()
