import unittest
from problem1 import calculate


class TestCalculateMethod(unittest.TestCase):

    def test_none(self):
        self.assertEqual(calculate(5), [])

    def test_single(self):
        self.assertEqual(calculate(7), [(3, 4, 5)])

    def test_several(self):
        self.assertEqual(calculate(50), [(3, 4, 5), (5, 12, 13), (6, 8, 10), (7, 24, 25), (8, 15, 17),
                                         (9, 12, 15), (9, 40, 41), (10, 24, 26), (12, 16, 20), (12, 35, 37),
                                         (15, 20, 25), (15, 36, 39), (16, 30, 34), (18, 24, 30), (20, 21, 29),
                                         (21, 28, 35), (24, 32, 40), (27, 36, 45)])

    def test_zero(self):
        self.assertEqual(calculate(0), [])

    def test_negative(self):
        self.assertEqual(calculate(-10), [])

    def test_one(self):
        self.assertEqual(calculate(1), [])

    def test_boundary_six(self):
        self.assertEqual(calculate(6), [(3, 4, 5)])

    def test_boundary_eleven(self):
        self.assertEqual(calculate(11), [(3, 4, 5), (6, 8, 10)])

    def test_boundary_fourteen(self):
        self.assertEqual(calculate(14), [(3, 4, 5), (5, 12, 13), (6, 8, 10)])

    def test_string(self):
        with self.assertRaises(TypeError):
            calculate("10")

    def test_float(self):
        with self.assertRaises(TypeError):
            calculate(10.5)


if __name__ == '__main__':
    unittest.main()
    