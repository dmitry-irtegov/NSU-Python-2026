import numpy as np
import uuid


def cummulative_sum(nums: list[int | float]) -> list[int | float]:
    res = [0]

    for num in nums:
        res.append(res[-1] + num)

    return res


def test_cummulative_sum() -> None:
    print(cummulative_sum([1, 2, 3]))
    random_numbers = [uuid.uuid4().int for _ in range(10)]

    assert np.array_equal(cummulative_sum(random_numbers)[1:], np.cumsum(random_numbers))


if __name__ == "__main__":
    test_cummulative_sum()
