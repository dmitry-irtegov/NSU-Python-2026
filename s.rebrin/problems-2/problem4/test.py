import unittest
from main import find_in_pi_stream_regex


class TestPiSearch(unittest.TestCase):
    FILE = "pi.txt"

    def check_positions(self, pattern: str, total_expected: int):
        total, positions = find_in_pi_stream_regex(self.FILE, pattern)
        self.assertEqual(total, total_expected)

        positions_set = set(positions)
        results = {}

        digit_pos = 0

        with open(self.FILE, "r") as f:
            pref = f.read(2)
            if pref == "3.":
                pref = ""
            while True:
                chunk = pref + f.read(1024 * 1024)
                if not chunk:
                    break

                digits = "".join(c for c in chunk if c.isdigit())

                i = 0
                while i < len(digits):
                    if digit_pos in positions_set:
                        results[digit_pos] = digits[i : i + len(pattern)]
                    digit_pos += 1
                    i += 1

        for pos in positions:
            self.assertEqual(results[pos], pattern)

    def test_145322(self):
        self.check_positions("145322", 4)

    def test_141592(self):
        self.check_positions("141592", 4)
        total, positions = find_in_pi_stream_regex(self.FILE, "141592")
        self.assertEqual(positions[0], 0)

    def test_single_digit(self):
        self.check_positions("1", 419139)

    def test_123(self):
        self.check_positions("123", 4185)

    def test_111(self):
        self.check_positions("111", 4172)

    def test_large_pattern(self):
        self.check_positions("4623462346634", 0)

    def test_empty_pattern(self):
        with self.assertRaises(ValueError):
            find_in_pi_stream_regex(self.FILE, "")


if __name__ == "__main__":
    unittest.main()
