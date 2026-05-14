import unittest

class Table:
    def __init__(self, data):
        self.data = [list(row) for row in data]

    def head(self, n):
        return Table(self.data[:n])

    def tail(self, n):
        return Table(self.data[-n:])

    def get_rows(self, indices):
        return Table([self.data[i] for i in indices])

    def concat_rows(self, other):
        return Table(self.data + other.data)

    def concat_cols(self, other):
        return Table([r1 + r2 for r1, r2 in zip(self.data, other.data)])

    def get_cols(self, indices):
        return Table([[row[i] for i in indices] for row in self.data])

    def __eq__(self, other):
        if not isinstance(other, Table):
            return False
        return self.data == other.data

    def __repr__(self):
        return f"Table({self.data})"


class TestTable(unittest.TestCase):
    def test_head(self):
        t = Table([[1, 2], [3, 4], [5, 6]])
        self.assertEqual(t.head(2), Table([[1, 2], [3, 4]]))

    def test_tail(self):
        t = Table([[1, 2], [3, 4], [5, 6]])
        self.assertEqual(t.tail(2), Table([[3, 4], [5, 6]]))

    def test_get_rows(self):
        t = Table([[1, 2], [3, 4], [5, 6]])
        self.assertEqual(t.get_rows([0, 2]), Table([[1, 2], [5, 6]]))

    def test_concat_rows(self):
        t1 = Table([[1, 2], [3, 4]])
        t2 = Table([[5, 6], [7, 8]])
        self.assertEqual(t1.concat_rows(t2), Table([[1, 2], [3, 4], [5, 6], [7, 8]]))

    def test_concat_cols(self):
        t1 = Table([[1, 2], [3, 4]])
        t2 = Table([[5], [6]])
        self.assertEqual(t1.concat_cols(t2), Table([[1, 2, 5], [3, 4, 6]]))

    def test_get_cols(self):
        t = Table([[1, 2, 3], [4, 5, 6]])
        self.assertEqual(t.get_cols([0, 2]), Table([[1, 3], [4, 6]]))

if __name__ == '__main__':
    unittest.main()