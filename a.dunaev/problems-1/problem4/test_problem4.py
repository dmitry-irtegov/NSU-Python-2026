import importlib.util
import pathlib
import subprocess
import unittest
from unittest.mock import patch


MODULE_PATH = pathlib.Path(__file__).with_name("problem4.py")
SPEC = importlib.util.spec_from_file_location("problem4", MODULE_PATH)
problem4 = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(problem4)


EXPECTED_TEXT = """Ten green bottles sitting on the wall,
Ten green bottles sitting on the wall,
And if one green bottle should accidentally fall,
There’ll be nine green bottles sitting on the wall.

Nine green bottles sitting on the wall,
Nine green bottles sitting on the wall,
And if one green bottle should accidentally fall,
There’ll be eight green bottles sitting on the wall.

Eight green bottles sitting on the wall,
Eight green bottles sitting on the wall,
And if one green bottle should accidentally fall,
There’ll be seven green bottles sitting on the wall.

Seven green bottles sitting on the wall,
Seven green bottles sitting on the wall,
And if one green bottle should accidentally fall,
There’ll be six green bottles sitting on the wall.

Six green bottles sitting on the wall,
Six green bottles sitting on the wall,
And if one green bottle should accidentally fall,
There’ll be five green bottles sitting on the wall.

Five green bottles sitting on the wall,
Five green bottles sitting on the wall,
And if one green bottle should accidentally fall,
There’ll be four green bottles sitting on the wall.

Four green bottles sitting on the wall,
Four green bottles sitting on the wall,
And if one green bottle should accidentally fall,
There’ll be three green bottles sitting on the wall.

Three green bottles sitting on the wall,
Three green bottles sitting on the wall,
And if one green bottle should accidentally fall,
There’ll be two green bottles sitting on the wall.

Two green bottles sitting on the wall,
Two green bottles sitting on the wall,
And if one green bottle should accidentally fall,
There’ll be one green bottle sitting on the wall.

One green bottle sitting on the wall,
One green bottle sitting on the wall,
And if one green bottle should accidentally fall,
There’ll be no green bottles sitting on the wall.
"""


class Problem4Tests(unittest.TestCase):
    def test_song_output_matches_full_text_with_custom_print(self) -> None:
        parts = []

        def custom_print(*args, sep=" ", end="\n") -> None:
            parts.append(sep.join(map(str, args)) + end)

        with patch("builtins.print", custom_print):
            problem4.sing_song()

        self.assertEqual("".join(parts), EXPECTED_TEXT)

    def test_script_output_matches_full_text(self) -> None:
        completed = subprocess.run(
            ["python3", str(MODULE_PATH)],
            check=True,
            capture_output=True,
            text=True,
        )

        self.assertEqual(completed.stdout, EXPECTED_TEXT)


if __name__ == "__main__":
    unittest.main()
