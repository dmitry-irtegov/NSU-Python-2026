import os
import tempfile
import unittest
from problem3 import get_sorted_files

class TestFileSorter(unittest.TestCase):
    def setUp(self) -> None:
        self.test_dir = tempfile.TemporaryDirectory()
        self.dir_path: str = self.test_dir.name

        self.create_file("a_small.txt", 10)
        self.create_file("b_small.txt", 10)
        self.create_file("c_large.txt", 100)
        self.create_file("d_medium.txt", 50)
        self.create_file("e_empty.txt", 0)

        os.mkdir(os.path.join(self.dir_path, "sub_dir"))

    def create_file(self, name: str, size: int) -> None:
        file_path: str = os.path.join(self.dir_path, name)
        with open(file_path, 'wb') as f:
            f.write(b'0' * size)

    def tearDown(self) -> None:
        self.test_dir.cleanup()

    def test_get_sorted_files(self) -> None:
        expected_order: list[tuple[str, int]] = [
            ("c_large.txt", 100),
            ("d_medium.txt", 50),
            ("a_small.txt", 10),
            ("b_small.txt", 10),
            ("e_empty.txt", 0)
        ]

        result: list[tuple[str, int]] = get_sorted_files(self.dir_path)
        self.assertEqual(result, expected_order)

    def test_invalid_directory(self) -> None:
        with self.assertRaises(ValueError):
            get_sorted_files(os.path.join(self.dir_path, "non_existent_dir"))

if __name__ == '__main__':
    unittest.main()