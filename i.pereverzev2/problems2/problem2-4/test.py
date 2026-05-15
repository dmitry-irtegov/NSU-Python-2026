import unittest
import random
from io import StringIO
from unittest.mock import patch
from problem4 import find_indices, run_search


class TestFindIndices(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with open("pi.txt", "r") as f:
            cls.pi_digits = f.read().strip()

    def test_random_sequences(self):
        random.seed(42)
        for _ in range(50):
            length = random.randint(1, 10)
            seq = "".join(str(random.randint(0, 9)) for _ in range(length))
            indices = find_indices(self.pi_digits, seq)
            for idx in indices:
                self.assertEqual(self.pi_digits[idx : idx + length], seq)

    def test_specific_sequences(self):
        cases = ["4564", "0", "329042", "123", "1415", "1000000", "9999999"]
        for seq in cases:
            indices = find_indices(self.pi_digits, seq)
            for idx in indices:
                self.assertEqual(self.pi_digits[idx : idx + len(seq)], seq)

    def test_empty_sequence(self):
        self.assertEqual(find_indices(self.pi_digits, ""), [])


class TestRunSearch(unittest.TestCase):
    def run_cli(self, inputs):
        with patch("builtins.input", side_effect=inputs), patch(
            "sys.stdout", new_callable=StringIO
        ) as mock_out:
            run_search()
            return mock_out.getvalue()

    def test_cli_found_output(self):
        self.assertIn("Found 396 results.", self.run_cli(["4564", ""]))

    def test_cli_not_found_output(self):
        self.assertIn("Found 0 results.", self.run_cli(["1000000", ""]))

    def test_cli_keyboard_interrupt(self):
        with patch("builtins.input", side_effect=KeyboardInterrupt), patch(
            "sys.stdout", new_callable=StringIO
        ):
            self.assertIsNone(run_search())


if __name__ == "__main__":
    unittest.main()
