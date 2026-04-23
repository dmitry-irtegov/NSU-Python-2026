import unittest

def cumsum(seq):
    cumulative_sum = [0]
    current_sum = 0
    for num in seq:
        current_sum += num
        cumulative_sum.append(current_sum)
    return cumulative_sum

class TestCumsum(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(cumsum([]), [0])

    def test_single_element(self):
        self.assertEqual(cumsum([5]), [0, 5])
        self.assertEqual(cumsum([-3]), [0, -3])

    def test_all_positive(self):
        self.assertEqual(cumsum([1, 2, 3]), [0, 1, 3, 6])

    def test_all_negative(self):
        self.assertEqual(cumsum([-1, -2, -3]), [0, -1, -3, -6])

    def test_mixed_numbers(self):
        self.assertEqual(cumsum([1, -1, 2, -2]), [0, 1, 0, 2, 0])

    def test_all_zeros(self):
        self.assertEqual(cumsum([0, 0, 0]), [0, 0, 0, 0])

    def test_repeated_elements(self):
        self.assertEqual(cumsum([5, 5, 5]), [0, 5, 10, 15])
        self.assertEqual(cumsum([1, 1, 1, 1]), [0, 1, 2, 3, 4])

    def test_large_numbers(self):
        self.assertEqual(cumsum([10**18, 10**18]), [0, 10**18, 2*10**18])
        self.assertEqual(cumsum([-10**18, -10**18]), [0, -10**18, -2*10**18])

    def test_input_immutability(self):
        lst = [1, 2, 3]
        cumsum(lst)
        self.assertEqual(lst, [1, 2, 3])

if __name__ == '__main__':
    unittest.main()