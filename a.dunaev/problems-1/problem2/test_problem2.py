import importlib.util
import pathlib
import random
import unittest


MODULE_PATH = pathlib.Path(__file__).with_name("problem2.py")
SPEC = importlib.util.spec_from_file_location("problem2", MODULE_PATH)
problem2 = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(problem2)


class LimitTests(unittest.TestCase):
    def test_random_values_with_seed(self) -> None:
        random.seed(42)
        data = [random.randint(-20, 20) for _ in range(20)]
        left, right = sorted((random.randint(-10, 0), random.randint(1, 10)))
        expected = [min(max(x, left), right) for x in data]

        result = problem2.limit(data, left, right)

        self.assertEqual(result, expected)

    def test_keeps_values_at_boundaries(self) -> None:
        data = [1, 2, 3]

        result = problem2.limit(data, 1, 3)

        self.assertEqual(result, [1, 2, 3])

    def test_returns_empty_list_for_empty_input(self) -> None:
        self.assertEqual(problem2.limit([], 0, 10), [])

    def test_does_not_modify_source_list(self) -> None:
        data = [-5, 0, 5]

        _ = problem2.limit(data, -2, 2)

        self.assertEqual(data, [-5, 0, 5])


if __name__ == "__main__":
    unittest.main()
