import unittest

class Table:
    def __init__(self, data):
        self.data = [row[:] for row in data]

    def head(self, n):
        return Table(self.data[:n])

    def tail(self, n):
        if n == 0:
            return Table([])
        return Table(self.data[-n:])

    def select_rows(self, indices):
        return Table([self.data[i] for i in indices])

    def concat_rows(self, other):
        return Table(self.data + other.data)

    def concat_cols(self, other):
        result = []
        for r1, r2 in zip(self.data, other.data):
            result.append(r1 + r2)
        return Table(result)

    def select_cols(self, indices):
        result = []
        for row in self.data:
            result.append([row[i] for i in indices])
        return Table(result)

    def __eq__(self, other):
        return self.data == other.data

    def __repr__(self):
        return f"Table({self.data})"

class TestTable(unittest.TestCase):

    def setUp(self):
        self.table = Table([
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9],
            [10, 11, 12]
        ])

    def test_head(self):
        expected = Table([
            [1, 2, 3],
            [4, 5, 6]
        ])
        self.assertEqual(self.table.head(2), expected)

    def test_tail(self):
        expected = Table([
            [7, 8, 9],
            [10, 11, 12]
        ])
        self.assertEqual(self.table.tail(2), expected)

    def test_zero_tail(self):
        expected = Table([])
        self.assertEqual(self.table.tail(0), expected)

    def test_select_rows(self):
        expected = Table([
            [1, 2, 3],
            [7, 8, 9]
        ])
        self.assertEqual(self.table.select_rows([0, 2]), expected)

    def test_concat_rows(self):
        other = Table([
            [13, 14, 15]
        ])
        expected = Table([
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9],
            [10, 11, 12],
            [13, 14, 15]
        ])
        self.assertEqual(self.table.concat_rows(other), expected)

    def test_concat_cols(self):
        other = Table([
            [100],
            [200],
            [300],
            [400]
        ])
        expected = Table([
            [1, 2, 3, 100],
            [4, 5, 6, 200],
            [7, 8, 9, 300],
            [10, 11, 12, 400]
        ])
        self.assertEqual(self.table.concat_cols(other), expected)

    def test_select_cols(self):
        expected = Table([
            [1, 3],
            [4, 6],
            [7, 9],
            [10, 12]
        ])
        self.assertEqual(self.table.select_cols([0, 2]), expected)

if __name__ == "__main__":
    unittest.main()