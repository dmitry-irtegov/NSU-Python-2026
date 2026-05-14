import unittest

from table import Table


class TestTable(unittest.TestCase):
    def setUp(self):
        self.t = Table([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])

    def test_head(self):
        self.assertEqual(self.t.head(2), Table([[1, 2, 3], [4, 5, 6]]))
        self.assertEqual(self.t.head(0), Table())
        self.assertEqual(self.t.head(100), self.t)
        self.assertEqual(Table().head(3), Table())

    def test_tail(self):
        self.assertEqual(self.t.tail(2), Table([[7, 8, 9], [10, 11, 12]]))
        self.assertEqual(self.t.tail(0), Table())
        self.assertEqual(self.t.tail(100), self.t)
        self.assertEqual(Table().tail(3), Table())

    def test_select_rows(self):
        self.assertEqual(self.t.select_rows([2, 0, 0]), Table([[7, 8, 9], [1, 2, 3], [1, 2, 3]]))
        self.assertEqual(self.t.select_rows([]), Table())
        self.assertEqual(self.t.select_rows([-1]), Table([[10, 11, 12]]))

    def test_select_columns(self):
        self.assertEqual(self.t.select_columns([2, 0]), Table([[3, 1], [6, 4], [9, 7], [12, 10]]))
        self.assertEqual(self.t.select_columns([0, 0]), Table([[1, 1], [4, 4], [7, 7], [10, 10]]))
        self.assertEqual(self.t.select_columns([]), Table([[], [], [], []]))
        self.assertEqual(Table().select_columns([0]), Table())

    def test_concat_rows(self):
        a = Table([[1, 2]])
        b = Table([[3, 4], [5, 6]])
        self.assertEqual(a.concat_rows(b), Table([[1, 2], [3, 4], [5, 6]]))
        self.assertEqual(a.concat_rows(Table()), a)
        self.assertEqual(Table().concat_rows(Table()), Table())

    def test_concat_cols(self):
        a = Table([[1, 2], [3, 4]])
        b = Table([[5], [6]])
        self.assertEqual(a.concat_cols(b), Table([[1, 2, 5], [3, 4, 6]]))
        self.assertEqual(Table().concat_cols(Table()), Table())

    def test_dunder(self):
        self.assertEqual(len(self.t), 4)
        self.assertEqual(self.t[1], [4, 5, 6])
        self.assertEqual(self.t[1:3], Table([[4, 5, 6], [7, 8, 9]]))
        self.assertEqual(list(self.t), [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
        self.assertNotEqual(self.t, [[1, 2, 3]])


if __name__ == "__main__":
    unittest.main()
