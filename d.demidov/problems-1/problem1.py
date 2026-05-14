import unittest
import uuid
from collections.abc import Sequence

import numpy as np


def cummulative_sum(nums: Sequence[int | float]) -> list[int | float]:
    res: list[int | float] = [0]

    num: int | float
    for num in nums:
        res.append(res[-1] + num)

    return res


class TestCummulativeSum(unittest.TestCase):
    def test_cummulative_sum(self) -> None:
        print(cummulative_sum([1, 2, 3]))
        random_numbers: list[int] = [uuid.uuid4().int for _ in range(10)]

        left_array = np.array(cummulative_sum(random_numbers)[1:])
        right_array = np.array(np.cumsum(random_numbers))
        self.assertTrue(np.array_equal(left_array, right_array))


if __name__ == "__main__":
    unittest.main()
