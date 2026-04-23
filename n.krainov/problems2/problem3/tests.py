import os
import shutil
import unittest
import tempfile
from problem3 import get_sorted_files

class TestGetSortedFilesContent(unittest.TestCase):
    def setUp(self):
        self.tmpdir = tempfile.mkdtemp()

    def tearDown(self):
        shutil.rmtree(self.tmpdir)

    def create_file(self, name, content=""):
        path = os.path.join(self.tmpdir, name)
        with open(path, "w") as f:
            f.write(content)
        return path

    def test_filename_in_result(self):
        self.create_file("hello.txt", "abc")
        names = [name for name, _ in get_sorted_files(self.tmpdir)]
        self.assertIn("hello.txt", names)

    def test_filesize_correct(self):
        self.create_file("hello.txt", "abc")
        result = dict(get_sorted_files(self.tmpdir))
        self.assertEqual(result["hello.txt"], 3)

    def test_directories_not_included(self):
        subdir = os.path.join(self.tmpdir, "subdir")
        os.mkdir(subdir)
        self.create_file("file.txt", "x")
        names = [name for name, _ in get_sorted_files(self.tmpdir)]
        self.assertNotIn("subdir", names)

    def test_all_files_included(self):
        self.create_file("a.txt", "x")
        self.create_file("b.txt", "xx")
        self.create_file("c.txt", "xxx")
        self.assertEqual(len(get_sorted_files(self.tmpdir)), 3)


class TestGetSortedFilesSorting(unittest.TestCase):
    def setUp(self):
        self.tmpdir = tempfile.mkdtemp()

    def tearDown(self):
        shutil.rmtree(self.tmpdir)

    def _create_file(self, name, content=""):
        path = os.path.join(self.tmpdir, name)
        with open(path, "w") as f:
            f.write(content)

    def test_sorted_by_size_ascending(self):
        self._create_file("big.txt",    "x" * 100)
        self._create_file("small.txt",  "x" * 10)
        self._create_file("medium.txt", "x" * 50)
        sizes = [size for _, size in get_sorted_files(self.tmpdir)]
        self.assertEqual(sizes, sorted(sizes))

    def test_same_size_sorted_by_name(self):
        self._create_file("b.txt", "xx")
        self._create_file("a.txt", "xx")
        self._create_file("c.txt", "xx")
        names = [name for name, _ in get_sorted_files(self.tmpdir)]
        self.assertEqual(names, ["a.txt", "b.txt", "c.txt"])

    def test_size_takes_priority_over_name(self):
        self._create_file("a.txt", "xxx")
        self._create_file("b.txt", "x")
        result = get_sorted_files(self.tmpdir)
        self.assertEqual(result[0][0], "b.txt")
        self.assertEqual(result[1][0], "a.txt")

if __name__ == '__main__':
    unittest.main()
