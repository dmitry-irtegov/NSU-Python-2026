import unittest
import tempfile
from pathlib import Path
from problem3 import list_files_sorted

class TestFileSorting(unittest.TestCase):

    def create_file(self, directory, name, size):
        path = Path(directory) / name
        with open(path, "wb") as f:
            f.write(b"a" * size)
        return path

    def test_sort_by_size(self):
        with tempfile.TemporaryDirectory() as tmp:
            self.create_file(tmp, "a.txt", 100)
            self.create_file(tmp, "b.txt", 300)
            self.create_file(tmp, "c.txt", 200)

            result = list_files_sorted(tmp)

            expected = [
                ("b.txt", 300),
                ("c.txt", 200),
                ("a.txt", 100)
            ]

            self.assertEqual(result, expected)

    def test_sort_by_name_if_same_size(self):
        with tempfile.TemporaryDirectory() as tmp:
            self.create_file(tmp, "b.txt", 100)
            self.create_file(tmp, "a.txt", 100)
            self.create_file(tmp, "c.txt", 100)

            result = list_files_sorted(tmp)

            expected = [
                ("a.txt", 100),
                ("b.txt", 100),
                ("c.txt", 100)
            ]

            self.assertEqual(result, expected)

    def test_empty_directory(self):
        with tempfile.TemporaryDirectory() as tmp:
            result = list_files_sorted(tmp)
            self.assertEqual(result, [])

if __name__ == "__main__":
    unittest.main()