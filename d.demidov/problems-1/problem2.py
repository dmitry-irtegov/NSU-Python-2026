import pytest


def clamp_array_to_bounds(arr, lower_bound, upper_bound):
    if lower_bound > upper_bound:
        raise ValueError("Lower bound must be less than upper bound")

    result = []

    for x in arr:
        if x > upper_bound:
            result.append(upper_bound)
        elif x < lower_bound:
            result.append(lower_bound)
        else:
            result.append(x)
    return result


def test_empty():
    original_list = []
    result_list = clamp_array_to_bounds(original_list, -10, 10)
    expected_list = []
    assert result_list == expected_list


def test_lower_bound():
    original_list = [1, 2, 3, 4, 5]
    result_list = clamp_array_to_bounds(original_list, 3, 10)
    expected_list = [3, 3, 3, 4, 5]
    assert result_list == expected_list


def test_upper_bound():
    original_list = [1, 2, 3, 4, 5]
    result_list = clamp_array_to_bounds(original_list, -10, 3)
    expected_list = [1, 2, 3, 3, 3]
    assert result_list == expected_list


def test_invalid_args():
    original_list = [1, 2, 3, 4, 5]
    with pytest.raises(ValueError):
        clamp_array_to_bounds(original_list, 5, -5)


def test_original_list_unchanged():
    original_list = [1, 2, 3, 4, 5]
    clamp_array_to_bounds(original_list, 1, 5)
    assert original_list == [1, 2, 3, 4, 5]
