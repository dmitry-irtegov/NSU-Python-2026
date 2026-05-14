import unittest


def clamp_array_to_bounds(
        arr: list[int | float],
        lower_bound: int | float,
        upper_bound: int | float,
) -> list[int | float]:
    if lower_bound > upper_bound:
        raise ValueError("Lower bound must be less than upper bound")

    result: list[int | float] = []

    x: int | float
    for x in arr:
        if x > upper_bound:
            result.append(upper_bound)
        elif x < lower_bound:
            result.append(lower_bound)
        else:
            result.append(x)
    return result


class TestClampArrayToBounds(unittest.TestCase):
    def test_empty(self) -> None:
        original_list: list[int | float] = []
        result_list: list[int | float] = clamp_array_to_bounds(original_list, -10, 10)
        expected_list: list[int | float] = []
        self.assertEqual(result_list, expected_list)

    def test_lower_bound(self) -> None:
        original_list: list[int | float] = [1, 2, 3, 4, 5]
        result_list: list[int | float] = clamp_array_to_bounds(original_list, 3, 10)
        expected_list: list[int | float] = [3, 3, 3, 4, 5]
        self.assertEqual(result_list, expected_list)

    def test_upper_bound(self) -> None:
        original_list: list[int | float] = [1, 2, 3, 4, 5]
        result_list: list[int | float] = clamp_array_to_bounds(original_list, -10, 3)
        expected_list: list[int | float] = [1, 2, 3, 3, 3]
        self.assertEqual(result_list, expected_list)

    def test_invalid_args(self) -> None:
        original_list: list[int | float] = [1, 2, 3, 4, 5]
        with self.assertRaises(ValueError):
            clamp_array_to_bounds(original_list, 5, -5)

    def test_original_list_unchanged(self) -> None:
        original_list: list[int | float] = [1, 2, 3, 4, 5]
        clamp_array_to_bounds(original_list, 1, 5)
        expected: list[int | float] = [1, 2, 3, 4, 5]
        self.assertEqual(original_list, expected)


if __name__ == "__main__":
    unittest.main()
