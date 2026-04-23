import unittest


class Table:
    def __init__(self, rows):
        self._rows = tuple(tuple(row) for row in rows)

    def head(self, n):
        return Table(self._rows[:n])

    def tail(self, n):
        if n == 0:
            return Table([])
        return Table(self._rows[-n:])

    def select_rows(self, indices):
        return Table((self._rows[i] for i in indices))

    def concat_rows(self, other):
        return Table(self._rows + other._rows)

    def concat_columns(self, other):
        return Table((row1 + row2 for row1, row2 in zip(self._rows, other._rows)))

    def select_columns(self, indices):
        return Table(((row[i] for i in indices) for row in self._rows))

    def __eq__(self, other):
        if not isinstance(other, Table):
            return False
        return self._rows == other._rows


class TestTable(unittest.TestCase):
    def test_head(self):
        table = Table(((1, 2), (3, 4), (5, 6)))
        self.assertEqual(table.head(2), Table(((1, 2), (3, 4))))

    def test_tail(self):
        table = Table(((1, 2), (3, 4), (5, 6)))
        self.assertEqual(table.tail(2), Table(((3, 4), (5, 6))))

    def test_select_rows(self):
        table = Table(((10, 20), (30, 40), (50, 60)))
        self.assertEqual(table.select_rows((0, 2)), Table(((10, 20), (50, 60))))

    def test_concat_rows(self):
        t1 = Table(((1, 2), (3, 4)))
        t2 = Table(((5, 6), (7, 8)))
        self.assertEqual(
            t1.concat_rows(t2),
            Table(((1, 2), (3, 4), (5, 6), (7, 8)))
        )

    def test_concat_columns(self):
        t1 = Table(((1, 2), (3, 4)))
        t2 = Table(((5, 6), (7, 8)))
        self.assertEqual(
            t1.concat_columns(t2),
            Table((
                (1, 2, 5, 6),
                (3, 4, 7, 8)
            ))
        )

    def test_select_columns(self):
        table = Table((
            (1, 2, 3),
            (4, 5, 6),
            (7, 8, 9)
        ))
        self.assertEqual(
            table.select_columns((0, 2)),
            Table((
                (1, 3),
                (4, 6),
                (7, 9)
            ))
        )

    def test_equality(self):
        self.assertEqual(
            Table(((1, 2), (3, 4))),
            Table(((1, 2), (3, 4)))
        )
        self.assertNotEqual(
            Table(((1, 2), (3, 4))),
            Table(((1, 2), (4, 3)))
        )

    def test_equality_with_non_table(self):
        self.assertNotEqual(Table(((1, 2),)), ((1, 2),))

    def test_head_all_rows(self):
        table = Table(((1,), (2,), (3,)))
        self.assertEqual(table.head(3), table)

    def test_tail_all_row(self):
        table = Table(((1, 2), (3, 4), (5, 6)))
        self.assertEqual(table.tail(3), table)

    def test_tail_zero_row(self):
        table = Table(((1, 2), (3, 4), (5, 6)))
        self.assertEqual(table.tail(0), Table(()))

    def test_select_columns_one_column(self):
        table = Table(((1, 2, 3), (4, 5, 6)))
        self.assertEqual(
            table.select_columns((1,)),
            Table(((2,), (5,)))
        )

    def test_large_sequence_concat_rows(self):
        t1 = Table((i,) for i in range(50))
        t2 = Table((i,) for i in range(50, 100))
        expected = Table((i,) for i in range(100))
        self.assertEqual(t1.concat_rows(t2), expected)

    def test_large_sequence_select_columns(self):
        table = Table(range(i, i + 4) for i in range(100))
        expected = Table((i, i + 2) for i in range(100))
        self.assertEqual(table.select_columns((0, 2)), expected)

    def test_create_from_iterator(self):
        rows = ((i, i + 1) for i in range(3))
        table = Table(rows)
        self.assertEqual(
            table,
            Table(((0, 1), (1, 2), (2, 3)))
        )

    def test_create_from_lazy_iterator(self):
        def row_generator():
            for i in range(3):
                yield [i, i + 1]

        table = Table(row_generator())
        self.assertEqual(
            table,
            Table(((0, 1), (1, 2), (2, 3)))
        )


if __name__ == "__main__":
    unittest.main()
