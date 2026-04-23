import unittest
import random
import math
from problem1 import cumulative_sums 

class TestCumulativeSums(unittest.TestCase):

    def test_empty(self):
        self.assertEqual(cumulative_sums([]), [0])

    def test_single(self):
        self.assertEqual(cumulative_sums([42.5]), [0, 42.5])

    def test_pos(self):
        self.assertEqual(cumulative_sums([1, 2, 3, 4]), [0, 1, 3, 6, 10])

    def test_neg(self):
        self.assertEqual(cumulative_sums([-1, -2, -3]), [0, -1, -3, -6])

    def test_mixed(self):
        self.assertEqual(cumulative_sums([1.5, -0.5, 2.0]), [0, 1.5, 1.0, 3.0])

    def test_rand(self):
        random.seed(42)
        seq = [random.uniform(-1000.0, 1000.0) for _ in range(1000)]
        result = cumulative_sums(seq)
        
        self.assertEqual(len(result), len(seq) + 1)
        self.assertEqual(result[0], 0)
        
        for i in range(1, len(result)):
            diff = result[i] - result[i-1]
            self.assertTrue(math.isclose(diff, seq[i-1], rel_tol=1e-9, abs_tol=1e-9))

if __name__ == "__main__":
    unittest.main(verbosity=2)