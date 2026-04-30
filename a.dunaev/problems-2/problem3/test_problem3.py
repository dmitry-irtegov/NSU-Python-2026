import io
import os
import sys
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path
import problem3


class SortFilesBySizeTests(unittest.TestCase):
    def test_sorts_files_by_size_descending_and_name_ascending(self):
        with tempfile.TemporaryDirectory() as tmp_dir:
            Path(tmp_dir, "beta.txt").write_text("12345", encoding="utf-8")
            Path(tmp_dir, "alpha.txt").write_text("12345", encoding="utf-8")
            Path(tmp_dir, "small.txt").write_text("1", encoding="utf-8")
            os.mkdir(Path(tmp_dir, "nested"))

            self.assertEqual(
                problem3.get_sorted_files(tmp_dir),
                [("alpha.txt", 5), ("beta.txt", 5), ("small.txt", 1)],
            )

    def test_format_files(self):
        self.assertEqual(
            problem3.format_files([("big.txt", 10), ("small.txt", 2)]),
            "big.txt 10\nsmall.txt 2",
        )

    def test_main_reads_directory_from_command_line_argument(self):
        with tempfile.TemporaryDirectory() as tmp_dir:
            Path(tmp_dir, "z.txt").write_text("1", encoding="utf-8")
            Path(tmp_dir, "a.txt").write_text("123", encoding="utf-8")

            stdout = io.StringIO()
            original_argv = sys.argv
            try:
                sys.argv = ["problem3.py", tmp_dir]
                with redirect_stdout(stdout):
                    problem3.main()
            finally:
                sys.argv = original_argv

        self.assertEqual(stdout.getvalue(), "a.txt 3\nz.txt 1\n")


if __name__ == "__main__":
    unittest.main()
