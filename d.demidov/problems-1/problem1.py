import unittest
from collections.abc import Sequence


def cummulative_sum(nums: Sequence[int | float]) -> list[int | float]:
    res: list[int | float] = [0]

    num: int | float
    for num in nums:
        res.append(res[-1] + num)

    return res


class TestCummulativeSum(unittest.TestCase):
    def test_simple_case(self) -> None:
        nums: list[int] = [1, 2, 3]
        res: list[int | float] = cummulative_sum(nums)
        expected: list[int] = [0, 1, 3, 6]
        self.assertEqual(res, expected)

    def test_empty_list(self) -> None:
        nums: list[int] = []
        res: list[int | float] = cummulative_sum(nums)
        expected: list[int] = [0]
        self.assertEqual(res, expected)

    def test_mixed_values(self) -> None:
        nums: list[int | float] = [2, -1, 0.5]
        res: list[int | float] = cummulative_sum(nums)
        expected: list[float] = [0, 2, 1, 1.5]
        self.assertEqual(res, expected)


if __name__ == "__main__":
    unittest.main()
