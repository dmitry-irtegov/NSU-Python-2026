import unittest


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


class TestClampArrayToBounds(unittest.TestCase):
    def test_empty(self):
        original_list = []
        result_list = clamp_array_to_bounds(original_list, -10, 10)
        expected_list = []
        self.assertEqual(result_list, expected_list)

    def test_lower_bound(self):
        original_list = [1, 2, 3, 4, 5]
        result_list = clamp_array_to_bounds(original_list, 3, 10)
        expected_list = [3, 3, 3, 4, 5]
        self.assertEqual(result_list, expected_list)

    def test_upper_bound(self):
        original_list = [1, 2, 3, 4, 5]
        result_list = clamp_array_to_bounds(original_list, -10, 3)
        expected_list = [1, 2, 3, 3, 3]
        self.assertEqual(result_list, expected_list)

    def test_invalid_args(self):
        original_list = [1, 2, 3, 4, 5]
        with self.assertRaises(ValueError):
            clamp_array_to_bounds(original_list, 5, -5)

    def test_original_list_unchanged(self):
        original_list = [1, 2, 3, 4, 5]
        clamp_array_to_bounds(original_list, 1, 5)
        self.assertEqual(original_list, [1, 2, 3, 4, 5])
