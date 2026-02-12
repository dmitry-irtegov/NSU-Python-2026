import random
import unittest
import numpy as np

def cut(a, b, elems):
    if (a > b) :
        return []
    return [ a if i < a else b if i > b else i for i in elems ]


class TestCut(unittest.TestCase):
    def test_cut(self):
        random.seed(42)
        n = random.randint(1, 10**6)
        b = random.randint(-1 * (10**6), 10**6)
        a = random.randint(-1 * (10**6), b)
        arr = []
        for i in range(n):
            np.append(arr, random.randint(-1 * (10**6), 10**6))
        np_arr = np.array(arr)
        my_res = np.array(cut(a, b, arr))
        np_res = np.clip(np_arr, a, b)
        self.assertTrue(np.array_equal(my_res, np_res))
        

if __name__ == "__main__":
    unittest.main()
