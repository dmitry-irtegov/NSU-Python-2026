import unittest
from random import randint, seed

from lab_1 import Table

seed(0)

def create_table():
    return Table([[12, 45, 78, 23, 56, 89, 34, 67, 90, 11, 44, 77], [33, 66, 99, 22, 55, 88, 31, 64, 97, 20, 53, 86],
                  [72, 15, 48, 81, 24, 57, 90, 33, 66, 99, 32, 65], [41, 74, 17, 50, 83, 26, 59, 92, 35, 68, 91, 24],
                  [98, 31, 64, 97, 30, 63, 96, 29, 52, 85, 18, 41], [55, 88, 21, 54, 87, 20, 53, 86, 19, 42, 75, 18],
                  [13, 46, 79, 12, 45, 78, 11, 44, 77, 10, 43, 76], [82, 25, 58, 91, 34, 67, 100, 33, 66, 99, 32, 65],
                  [39, 72, 15, 48, 81, 14, 47, 80, 13, 46, 79, 42], [57, 90, 23, 56, 89, 22, 55, 88, 21, 54, 87, 20],
                  [74, 17, 40, 73, 16, 49, 82, 25, 58, 91, 24, 57], [95, 28, 61, 94, 27, 60, 93, 26, 59, 92, 25, 58]])


def create_random_table(lines=3, rows=3):
    return Table([[randint(-500, 500) for _ in range(rows)] for _ in range(lines)])


class MyTestCase(unittest.TestCase):

    def test_head(self):
        table = create_table()
        head = table.head(2)
        table2 = Table([[12, 45, 78, 23, 56, 89, 34, 67, 90, 11, 44, 77], [33, 66, 99, 22, 55, 88, 31, 64, 97, 20, 53, 86]])
        self.assertEqual(head, table2)
        table2 = create_table()
        self.assertEqual(table, table2)

    def test_head_failed(self):
        with self.assertRaisesRegex(ValueError, "Cnt lines to return more than lines in table"):
            table = create_random_table()
            table.head(len(table.table) + 1)

        with self.assertRaisesRegex(ValueError, "Cnt lines to return more than lines in table"):
            table = create_random_table()
            table.head(-1)

    def test_tail(self):
        table = create_table()
        tail = table.tail(3)
        table2 = Table([[57, 90, 23, 56, 89, 22, 55, 88, 21, 54, 87, 20],
                  [74, 17, 40, 73, 16, 49, 82, 25, 58, 91, 24, 57], [95, 28, 61, 94, 27, 60, 93, 26, 59, 92, 25, 58]])
        self.assertEqual(tail, table2)
        table2 = create_table()
        self.assertEqual(table, table2)

    def test_tail_failed(self):
        with self.assertRaisesRegex(ValueError, "Cnt lines to return more than lines in table"):
            table = create_table()
            table.tail(len(table.table) + 1)

        with self.assertRaisesRegex(ValueError, "Cnt lines to return more than lines in table"):
            table = create_table()
            table.tail(-1)

    def test_get_lines(self):
        table = create_table()
        line_table = table.get_lines([number for number in range(1, len(table.table), 2)])
        table2 = Table([[33, 66, 99, 22, 55, 88, 31, 64, 97, 20, 53, 86],
                [41, 74, 17, 50, 83, 26, 59, 92, 35, 68, 91, 24],
                [55, 88, 21, 54, 87, 20, 53, 86, 19, 42, 75, 18],
                [82, 25, 58, 91, 34, 67, 100, 33, 66, 99, 32, 65],
                [57, 90, 23, 56, 89, 22, 55, 88, 21, 54, 87, 20],
                [95, 28, 61, 94, 27, 60, 93, 26, 59, 92, 25, 58]])
        self.assertEqual(line_table, table2)
        table2 = create_table()
        self.assertEqual(table, table2)

    def test_get_lines_failed(self):
        with self.assertRaisesRegex(ValueError, "line out of index"):
            table = create_table()
            lines = [number for number in range(1, len(table.table), 2)]
            lines[2] = -1
            table.get_lines(lines)

        with self.assertRaisesRegex(ValueError, "line out of index"):
            table = create_table()
            lines = [number for number in range(1, len(table.table), 2)]
            lines[4] = 13
            table.get_lines(lines)

    def test_row_selecting(self):
        table = create_table()
        row_table = table.get_rows([1, 2])
        ans = Table([[45, 78], [66, 99],
                  [15, 48], [74, 17],
                  [31, 64], [88, 21],
                  [46, 79], [25, 58],
                  [72, 15], [90, 23],
                  [17, 40], [28, 61]])
        self.assertEqual(row_table, ans)

    def test_line_adding(self):
        table1 = create_random_table()
        table2 = create_random_table(5, 3)
        sum_table1 = table1.right_line_add(table2)
        sum_table2 = table2.left_line_add(table1)
        self.assertEqual(sum_table1, sum_table2)
        self.assertEqual(sum_table1.head(3), table1)
        self.assertEqual(sum_table1.tail(5), table2)

    def test_row_adding(self):
        table1 = create_random_table()
        table2 = create_random_table(3, 5)
        sum_table1 = table1.right_row_add(table2)
        sum_table2 = table2.left_row_add(table1)
        self.assertEqual(sum_table1, sum_table2)
        self.assertEqual(sum_table1.get_rows([0, 1, 2]), table1)
        self.assertEqual(sum_table2.get_rows([3, 4, 5, 6, 7]), table2)


if __name__ == '__main__':
    unittest.main()
