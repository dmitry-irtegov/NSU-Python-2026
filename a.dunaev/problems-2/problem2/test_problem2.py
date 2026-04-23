import io
import os
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path
import problem2


class LatinEnglishDictionaryTests(unittest.TestCase):
    def test_inverts_dictionary_and_sorts_words(self):
        self.assertEqual(
            problem2.solve(
                "\n".join(
                    [
                        "apple - malum, pomum, popula",
                        "fruit - baca, bacca, popum",
                        "punishment - malum, multa",
                    ]
                )
            ),
            "\n".join(
                [
                    "baca - fruit",
                    "bacca - fruit",
                    "malum - apple, punishment",
                    "multa - punishment",
                    "pomum - apple",
                    "popula - apple",
                    "popum - fruit",
                ]
            ),
        )

    def test_supports_input_with_count_on_first_line(self):
        self.assertEqual(
            problem2.solve(
                "\n".join(
                    [
                        "3",
                        "apple - malum, pomum, popula",
                        "fruit - baca, bacca, popum",
                        "punishment - malum, multa",
                    ]
                )
            ),
            "\n".join(
                [
                    "baca - fruit",
                    "bacca - fruit",
                    "malum - apple, punishment",
                    "multa - punishment",
                    "pomum - apple",
                    "popula - apple",
                    "popum - fruit",
                ]
            ),
        )

    def test_main_reads_data_from_file(self):
        with tempfile.TemporaryDirectory() as tmp_dir:
            data_path = Path(tmp_dir) / "data.txt"
            data_path.write_text("dog - canis\ncat - felis\nwolf - canis\n", encoding="utf-8")

            stdout = io.StringIO()
            current_dir = os.getcwd()
            try:
                os.chdir(tmp_dir)
                with redirect_stdout(stdout):
                    problem2.main()
            finally:
                os.chdir(current_dir)

        self.assertEqual(stdout.getvalue(), "canis - dog, wolf\nfelis - cat")


if __name__ == "__main__":
    unittest.main()
