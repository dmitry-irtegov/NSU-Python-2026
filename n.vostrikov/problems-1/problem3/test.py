import unittest
from io import StringIO
from unittest.mock import patch

from problem3 import collatz


class TestOutput(unittest.TestCase):
    def test_collatz(self):
        with patch("sys.stdout", new=StringIO()) as mock_out:
            collatz(3)
            self.assertEqual(mock_out.getvalue(), "3->10->5->16->8->4->2->1\n")
            mock_out.truncate(0)
            mock_out.seek(0)
            collatz(6)
            self.assertEqual(
                mock_out.getvalue(),
                "6->3->10->5->16->8->4->2->1\n",
            )
            mock_out.truncate(0)
            mock_out.seek(0)
            collatz(-4)
            self.assertEqual(mock_out.getvalue(), "")

    def test_collatz_one(self):
        with patch("sys.stdout", new=StringIO()) as mock_out:
            collatz(1)
            self.assertEqual(mock_out.getvalue(), "1\n")

    def test_collatz_zero(self):
        with patch("sys.stdout", new=StringIO()) as mock_out:
            self.assertEqual(collatz(0), [])
            self.assertEqual(mock_out.getvalue(), "")


if __name__ == "__main__":
    unittest.main()
