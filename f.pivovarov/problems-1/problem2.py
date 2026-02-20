from random import randint, random
import unittest

def cut(numbers, a, b):
    return [a if x < a else b if x > b else x for x in numbers]


class TestCut(unittest.TestCase):

    def test_a_b_count(self):
        a, b, arr = self.get_a_b_arr()
        # кол-во a после применения функции ровняется кол-ву чисел <= a в исходном массиве
        self.assertTrue(cut(arr, a, b).count(a) == len([num for num in arr if num <= a]))
        # по аналогии для b
        self.assertTrue(cut(arr, a, b).count(b) == len([num for num in arr if num >= b]))

    def test_inbound_invariance(self):
        a, b, arr = self.get_a_b_arr()
        # подсписок где num >a и <b не изменяется
        self.assertTrue([num for num in cut(arr, a, b) if num > a and num < b] == [num for num in arr if num > a and num < b])

    def test_size_invariance(self):
        a, b, arr = self.get_a_b_arr()
        self.assertTrue(len(arr) == len(cut(arr, a, b)))

    def get_a_b_arr(self):
        size = randint(1, 1000)
        a = random()
        b = random()
        a, b = min(a, b), max(a, b)
        arr = [random() for i in range(size)]

        return a, b, arr

if __name__ == '__main__':
    unittest.main()
