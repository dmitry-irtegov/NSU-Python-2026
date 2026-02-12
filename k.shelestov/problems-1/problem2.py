import unittest

def clip_numbers(seq, lower_bound, upper_bound):
    if lower_bound > upper_bound:
        raise ValueError("Lower bound must be less than or equal to upper bound")

    res = []
    for num in seq:
        if num < lower_bound:
            res.append(lower_bound)
        elif num > upper_bound:
            res.append(upper_bound)
        else:
            res.append(num)
    return res

class TestClipNumbers(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(clip_numbers([], -50, 50), [])

    def test_single_element_inside_bounds(self):
        self.assertEqual(clip_numbers([7], 0, 20), [7])

    def test_same_bounds(self):
        self.assertEqual(clip_numbers([2, 4, 6, 8], 5, 5), [5, 5, 5, 5])

    def test_lower_bound_partial(self):
        self.assertEqual(clip_numbers([2, 5, 8], 4, 15), [4, 5, 8])

    def test_lower_bound_all(self):
        self.assertEqual(clip_numbers([10, 20, 15], 30, 40), [30, 30, 30])

    def test_upper_bound_partial(self):
        self.assertEqual(clip_numbers([3, 6, 9], 0, 5), [3, 5, 5])

    def test_upper_bound_all(self):
        self.assertEqual(clip_numbers([12, 18, 25], 0, 10), [10, 10, 10])

    def test_values_on_bounds(self):
        self.assertEqual(clip_numbers([5, 10, 15], 5, 15), [5, 10, 15])

    def test_elements_equal_to_bounds(self):
        self.assertEqual(clip_numbers([1, 50, 100], 1, 100), [1, 50, 100])

    def test_large_numbers(self):
        self.assertEqual(clip_numbers([-5000, 0, 5000], -100, 100), [-100, 0, 100])

    def test_negative_bounds(self):
        self.assertEqual(clip_numbers([-20, -10, 0, 10], -15, -5), [-15, -10, -5, -5])

    def test_bounds_including_zero(self):
        self.assertEqual(clip_numbers([-8, 0, 8], -3, 3), [-3, 0, 3])

    def test_no_bound_effect(self):
        self.assertEqual(clip_numbers([7, 8, 9], 0, 10), [7, 8, 9])

    def test_all_elements_within_bounds(self):
        self.assertEqual(clip_numbers([2, 4, 6], 1, 10), [2, 4, 6])

    def test_long_list(self):
        arr = list(range(-20, 21))  
        expected = [-5]*15 + list(range(-5, 6)) + [5]*15
        self.assertEqual(clip_numbers(arr, -5, 5), expected)

    def test_float_values(self):
        self.assertEqual(clip_numbers([0.2, 1.8, 2.5], 0.5, 2.0), [0.5, 1.8, 2.0])

    def test_invalid_args(self):
        with self.assertRaises(ValueError):
            clip_numbers([1, 2, 3], 10, 5)

    def test_original_list_unchanged(self):
        lst = [3, 7, 12]
        clip_numbers(lst, 5, 10)
        self.assertEqual(lst, [3, 7, 12])


if __name__ == "__main__":
    unittest.main()