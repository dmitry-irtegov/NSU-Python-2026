import unittest
from problem3 import collatz_seq

class TestCollatzSeqKnownValues(unittest.TestCase):
    def test_number_1(self):
        flag, seq = collatz_seq(1)
        self.assertTrue(flag)
        self.assertEqual(seq, [1])

    def test_number_2(self):
        flag, seq = collatz_seq(2)
        self.assertTrue(flag)
        self.assertEqual(seq, [2, 1])

    def test_number_3(self):
        flag, seq = collatz_seq(3)
        self.assertTrue(flag)
        self.assertEqual(seq, [3, 10, 5, 16, 8, 4, 2, 1])

    def test_number_6(self):
        flag, seq = collatz_seq(6)
        self.assertTrue(flag)
        self.assertEqual(seq, [6, 3, 10, 5, 16, 8, 4, 2, 1])

    def test_number_27_length(self):
        flag, seq = collatz_seq(27)
        self.assertTrue(flag)
        self.assertEqual(len(seq), 112)



class TestCollatzSeqMaxIter(unittest.TestCase):
    def test_exceeds_max_iter_returns_false(self):
        flag, seq = collatz_seq(3, maxIter=3)
        self.assertFalse(flag)
        self.assertEqual(seq, [])

    def test_exceeds_max_iter_returns_empty_list(self):
        _, seq = collatz_seq(3, maxIter=1)
        self.assertIsInstance(seq, list)
        self.assertEqual(len(seq), 0)

    def test_exact_max_iter_completes(self):
        flag, seq = collatz_seq(2, maxIter=1)
        self.assertTrue(flag)
        self.assertEqual(seq, [2, 1])

    def test_default_max_iter_large_number(self):
        flag, _ = collatz_seq(1_000_000)
        self.assertTrue(flag)

if __name__ == '__main__':
    unittest.main()
