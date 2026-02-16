import unittest
from random import randint
from lab_2 import bounds
class MyTestCase(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(bounds(1, 3, [0, 1, 2, 3, 4]), [1, 1, 2, 3, 3])

    def test_hard(self):
        lower = -500
        upper = 500
        nums = [randint(-1000000, 1000000) for i in range(1000000)]
        nums = bounds(lower, upper, nums)
        self.assertTrue(all(lower <= num <= upper for num in nums))


if __name__ == '__main__':
    unittest.main()
