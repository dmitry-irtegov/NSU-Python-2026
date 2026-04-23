import io
import os
import sys
import tempfile
import unittest
from contextlib import redirect_stderr, redirect_stdout
from unittest.mock import patch

import problem3


class TestListFilesBySize(unittest.TestCase):
    def test_empty_directory(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            self.assertEqual(problem3.list_files_by_size(tmpdir), [])

    def test_single_file(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            path = os.path.join(tmpdir, "a.txt")
            with open(path, "w", encoding="utf-8") as f:
                f.write("hello")

            self.assertEqual(problem3.list_files_by_size(tmpdir), [("a.txt", 5)])

    def test_sorted_by_size_descending(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            files = {
                "small.txt": "a",
                "medium.txt": "abcd",
                "large.txt": "abcdefgh",
            }

            for name, content in files.items():
                with open(os.path.join(tmpdir, name), "w", encoding="utf-8") as f:
                    f.write(content)

            self.assertEqual(problem3.list_files_by_size(tmpdir), [
                ("large.txt", 8),
                ("medium.txt", 4),
                ("small.txt", 1),
            ])

    def test_same_size_sorted_alphabetically(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            for name in ["c.txt", "a.txt", "b.txt"]:
                with open(os.path.join(tmpdir, name), "w", encoding="utf-8") as f:
                    f.write("xx")

            self.assertEqual(problem3.list_files_by_size(tmpdir), [
                ("a.txt", 2),
                ("b.txt", 2),
                ("c.txt", 2),
            ])

    def test_ignores_subdirectories(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            with open(os.path.join(tmpdir, "file.txt"), "w", encoding="utf-8") as f:
                f.write("data")

            os.mkdir(os.path.join(tmpdir, "subdir"))
            with open(os.path.join(tmpdir, "subdir", "nested.txt"), "w", encoding="utf-8") as f:
                f.write("nested")

            self.assertEqual(problem3.list_files_by_size(tmpdir), [
                ("file.txt", 4),
            ])

    def test_big_complex_example(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            contents = {
                "zeta.log": "1" * 12,
                "alpha.txt": "1" * 12,
                "notes.md": "1" * 7,
                "data.bin": "1" * 20,
                "readme.md": "1" * 7,
                "x.py": "1" * 1,
                "archive.tar": "1" * 20,
                "mid.txt": "1" * 10,
            }

            for name, content in contents.items():
                with open(os.path.join(tmpdir, name), "w", encoding="utf-8") as f:
                    f.write(content)

            os.mkdir(os.path.join(tmpdir, "folder"))
            with open(os.path.join(tmpdir, "folder", "inner.txt"), "w", encoding="utf-8") as f:
                f.write("ignore me")

            self.assertEqual(problem3.list_files_by_size(tmpdir), [
                ("archive.tar", 20),
                ("data.bin", 20),
                ("alpha.txt", 12),
                ("zeta.log", 12),
                ("mid.txt", 10),
                ("notes.md", 7),
                ("readme.md", 7),
                ("x.py", 1),
            ])

    def test_invalid_directory_type_raises(self):
        with self.assertRaises(TypeError):
            problem3.list_files_by_size(123)

    def test_empty_directory_name_raises(self):
        with self.assertRaises(ValueError):
            problem3.list_files_by_size("")

    def test_nonexistent_directory_raises(self):
        with self.assertRaises(ValueError):
            problem3.list_files_by_size("definitely_missing_directory_12345")


class TestFormatFiles(unittest.TestCase):
    def test_format_empty(self):
        self.assertEqual(problem3.format_files([]), "")

    def test_format_basic(self):
        self.assertEqual(
            problem3.format_files([("a.txt", 10), ("b.txt", 5)]),
            "a.txt 10\nb.txt 5"
        )

    def test_invalid_files_type_raises(self):
        with self.assertRaises(TypeError):
            problem3.format_files("not a list")

    def test_invalid_file_entry_raises(self):
        with self.assertRaises(ValueError):
            problem3.format_files(["a.txt"])


class TestMainIO(unittest.TestCase):
    def run_main_capture(self, argv):
        out_buf = io.StringIO()
        err_buf = io.StringIO()

        with (
            patch.object(sys, "argv", argv),
            redirect_stdout(out_buf),
            redirect_stderr(err_buf)
        ):
            problem3.main()

        return out_buf.getvalue(), err_buf.getvalue()

    def test_main_ok(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            with open(os.path.join(tmpdir, "b.txt"), "w", encoding="utf-8") as f:
                f.write("xx")
            with open(os.path.join(tmpdir, "a.txt"), "w", encoding="utf-8") as f:
                f.write("xxxx")

            out, err = self.run_main_capture(["problem3.py", tmpdir])
            self.assertEqual(err, "")
            self.assertEqual(out, "a.txt 4\nb.txt 2\n")

    def test_main_empty_directory(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            out, err = self.run_main_capture(["problem3.py", tmpdir])
            self.assertEqual(out, "")
            self.assertEqual(err, "")

    def test_main_invalid_argv_count_logs(self):
        out, err = self.run_main_capture(["problem3.py"])
        self.assertEqual(out, "")
        self.assertNotEqual(err, "")

    def test_main_nonexistent_directory_logs(self):
        out, err = self.run_main_capture(["problem3.py", "missing_directory_123"])
        self.assertEqual(out, "")
        self.assertNotEqual(err, "")

    def test_main_big_complex_example(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            contents = {
                "zeta.log": "1" * 12,
                "alpha.txt": "1" * 12,
                "notes.md": "1" * 7,
                "data.bin": "1" * 20,
                "readme.md": "1" * 7,
                "x.py": "1" * 1,
                "archive.tar": "1" * 20,
                "mid.txt": "1" * 10,
            }

            for name, content in contents.items():
                with open(os.path.join(tmpdir, name), "w", encoding="utf-8") as f:
                    f.write(content)

            os.mkdir(os.path.join(tmpdir, "folder"))
            with open(os.path.join(tmpdir, "folder", "inner.txt"), "w", encoding="utf-8") as f:
                f.write("ignore")

            out, err = self.run_main_capture(["problem3.py", tmpdir])
            self.assertEqual(err, "")
            self.assertEqual(
                out,
                "\n".join([
                    "archive.tar 20",
                    "data.bin 20",
                    "alpha.txt 12",
                    "zeta.log 12",
                    "mid.txt 10",
                    "notes.md 7",
                    "readme.md 7",
                    "x.py 1",
                ]) + "\n"
            )


if __name__ == "__main__":
    unittest.main()