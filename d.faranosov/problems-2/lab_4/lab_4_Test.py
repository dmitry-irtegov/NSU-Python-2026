import unittest
from lab_4 import get_stats

class MyTestCase(unittest.TestCase):
    def test(self):
        cases = [
            ("123", 4185, [1923, 2937, 2975, 3891, 6547]),
            ("1415", 424, [0, 6954, 29135, 45233, 79686]),
            ("1725", 366, [137, 9398, 29068, 40955, 71136]),
            ("21290", 37, [710, 74462, 88054, 388504, 522889]),
            ("08253344", 1, [826])
        ]

        for inp, exp, exp_list in cases:
            res_cnt, res_list = get_stats(inp)
            self.assertEqual(res_cnt, exp)
            self.assertEqual(res_list, exp_list)


if __name__ == '__main__':
    unittest.main()
