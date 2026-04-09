import importlib.util
import pathlib
import unittest


MODULE_PATH = pathlib.Path(__file__).with_name("problem3.py")
SPEC = importlib.util.spec_from_file_location("problem3", MODULE_PATH)
problem3 = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(problem3)


class Problem3Tests(unittest.TestCase):
    def test_collatz_sequence_for_one(self) -> None:
        self.assertEqual(problem3.collatz(1), [1])

    def test_collatz_sequence_for_even_start(self) -> None:
        self.assertEqual(problem3.collatz(6), [6, 3, 10, 5, 16, 8, 4, 2, 1])

    def test_format_sequence(self) -> None:
        self.assertEqual(problem3.format_seq(3), "3 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1")

    def test_non_positive_input_raises_value_error(self) -> None:
        with self.assertRaises(ValueError):
            problem3.collatz(0)


if __name__ == "__main__":
    unittest.main()
