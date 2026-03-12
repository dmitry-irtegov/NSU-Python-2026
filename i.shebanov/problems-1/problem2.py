#!/usr/bin/python3

def narrow_list(arr, lower_bound, upper_bound):
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


import unittest

class TestNarrowList(unittest.TestCase):
    def test_empty(self):
        original_list = []
        result_list = narrow_list(original_list, -10, 10)
        expected_list = []
        self.assertEqual(result_list, expected_list)

    def test_same_bounds(self):
        original_list = [1,2,3,4,5]
        result_list = narrow_list(original_list, 6, 6)
        expected_list = [6,6,6,6,6]
        self.assertEqual(result_list, expected_list)

    def test_lower_bound(self):
        original_list = [1,2,3,4,5]
        result_list = narrow_list(original_list, 3, 100)
        expected_list = [3,3,3,4,5]
        self.assertEqual(result_list, expected_list)
    
    def test_lower_bound_all(self):
        original_list = [4,6,3,4,5]
        result_list = narrow_list(original_list, 100, 150)
        expected_list = [100,100,100,100,100]
        self.assertEqual(result_list, expected_list)

    def test_upper_bound(self):
        original_list = [1,2,3,4,5]
        result_list = narrow_list(original_list, -10, 3)
        expected_list = [1,2,3,3,3]
        self.assertEqual(result_list, expected_list)

    def test_upper_bound_all(self):
        original_list = [4,6,3,4,5]
        result_list = narrow_list(original_list, -10, 3)
        expected_list = [3,3,3,3,3]
        self.assertEqual(result_list, expected_list)

    def test_values_on_bounds(self):
        original_list = [3,4,5]
        result_list = narrow_list(original_list, 3, 5)
        expected_list = [3,4,5]
        self.assertEqual(result_list, expected_list)

    def test_large_numbers(self):
        original_list = [-10**9, 0, 10**9]
        result_list = narrow_list(original_list, -5, 5)
        expected_list = [-5, 0, 5]
        self.assertEqual(result_list, expected_list)

    def test_no_bound_effect(self):
        original_list = [1,2,3,4,5]
        result_list = narrow_list(original_list, -10, 10)
        expected_list = [1,2,3,4,5]
        self.assertEqual(result_list, expected_list)

    def test_invalid_args(self):
        original_list = [1,2,3,4,5]
        with self.assertRaises(ValueError):
            narrow_list(original_list, 5, -5)

    def test_original_list_unchanged(self):
        original_list = [1,2,3]
        narrow_list(original_list, 2, 3)
        self.assertEqual(original_list, [1,2,3])
    


if __name__ == "__main__":
    unittest.main()
