import unittest
from io import StringIO
from unittest.mock import patch

from problem import print_song


class TestBottles(unittest.TestCase):
    def test_print_song(self):
        with open("song.txt", "r", encoding="utf-8") as f:
            expected = f.read()

        with patch("sys.stdout", new=StringIO()) as mock_out:
            print_song()
            actual = mock_out.getvalue()

        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()