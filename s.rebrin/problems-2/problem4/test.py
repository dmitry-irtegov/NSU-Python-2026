import unittest
from main import find_in_pi_stream


class TestPiSearch(unittest.TestCase):
    FILE = "pi.txt"

    def check_positions(self, pattern: str, total_expected: int):
        total, positions = find_in_pi_stream(self.FILE, pattern)
        self.assertEqual(total, total_expected)

        with open(self.FILE, "r") as f:
            for pos in positions:
                f.seek(pos + 2)
                chunk = f.read(len(pattern))
                self.assertEqual(chunk, pattern)

    def test_145322(self):
        self.check_positions("145322", 2)

    def test_141592(self):
        self.check_positions("141592", 4)
        total, positions = find_in_pi_stream(self.FILE, "141592")
        self.assertEqual(positions[0], 0)

    def test_single_digit(self):
        self.check_positions("1", 419139)

    def test_123(self):
        self.check_positions("123", 4079)

    def test_111(self):
        self.check_positions("111", 4044)

    def test_large_pattern(self):
        self.check_positions("4623462346634", 0)

    def test_empty_pattern(self):
        with self.assertRaises(ValueError):
            find_in_pi_stream(self.FILE, "")


if __name__ == "__main__":
    unittest.main()
