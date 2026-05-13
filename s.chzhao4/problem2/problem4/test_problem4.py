import unittest
from problem4 import find_all_occurrences


class TestPiSearch(unittest.TestCase):
    def test_find_all_occurrences_basic(self) -> None:
        text: str = "1415926535897932384626433832791415"
        result: list[int] = find_all_occurrences(text, "1415")
        self.assertEqual(result, [0, 30])

    def test_find_all_occurrences_overlapping(self) -> None:
        text: str = "1111"
        result: list[int] = find_all_occurrences(text, "11")
        self.assertEqual(result, [0, 1, 2])

    def test_find_all_occurrences_not_found(self) -> None:
        text: str = "123456"
        result: list[int] = find_all_occurrences(text, "999")
        self.assertEqual(result, [])

    def test_find_all_occurrences_single_char(self) -> None:
        text: str = "102030"
        result: list[int] = find_all_occurrences(text, "0")
        self.assertEqual(result, [1, 3, 5])


if __name__ == '__main__':
    unittest.main()