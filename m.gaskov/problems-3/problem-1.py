import unittest
from typing import Sequence, Self


class Table:
    def __init__(self: Self, rows: Sequence[Sequence[object]]) -> None:
        self._rows: list[list[object]] = [list(row) for row in rows]

    def head(self: Self, n: int) -> Self:
        return Table(self._rows[:n])

    def tail(self: Self, n: int) -> Self:
        if n == 0:
            return Table([])
        return Table(self._rows[-n:])

    def select_rows(self: Self, indices: Sequence[int]) -> Self:
        return Table([self._rows[i] for i in indices])

    def concat_rows(self: Self, other: Self) -> Self:
        return Table(self._rows + other._rows)

    def concat_columns(self: Self, other: Self) -> Self:
        return Table([row1 + row2 for row1, row2 in zip(self._rows, other._rows)])

    def select_columns(self: Self, indices: Sequence[int]) -> Self:
        return Table([[row[i] for i in indices] for row in self._rows])

    def __eq__(self: Self, other: object) -> bool:
        if not isinstance(other, Table):
            return False
        return self._rows == other._rows


class TestTable(unittest.TestCase):
    def test_head(self: Self) -> None:
        table: Table = Table([[1, 2], [3, 4], [5, 6]])
        self.assertEqual(table.head(2), Table([[1, 2], [3, 4]]))

    def test_tail(self: Self) -> None:
        table: Table = Table([[1, 2], [3, 4], [5, 6]])
        self.assertEqual(table.tail(2), Table([[3, 4], [5, 6]]))

    def test_select_rows(self: Self) -> None:
        table: Table = Table([[10, 20], [30, 40], [50, 60]])
        self.assertEqual(table.select_rows([0, 2]), Table([[10, 20], [50, 60]]))

    def test_concat_rows(self: Self) -> None:
        t1: Table = Table([[1, 2], [3, 4]])
        t2: Table = Table([[5, 6], [7, 8]])
        self.assertEqual(
            t1.concat_rows(t2),
            Table([[1, 2], [3, 4], [5, 6], [7, 8]])
        )

    def test_concat_columns(self: Self) -> None:
        t1: Table = Table([[1, 2], [3, 4]])
        t2: Table = Table([[5, 6], [7, 8]])
        self.assertEqual(
            t1.concat_columns(t2),
            Table([
                [1, 2, 5, 6],
                [3, 4, 7, 8]
            ])
        )

    def test_select_columns(self: Self) -> None:
        table: Table = Table([
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ])
        self.assertEqual(
            table.select_columns([0, 2]),
            Table([
                [1, 3],
                [4, 6],
                [7, 9]
            ])
        )

    def test_equality(self: Self) -> None:
        self.assertEqual(
            Table([[1, 2], [3, 4]]),
            Table([[1, 2], [3, 4]])
        )
        self.assertNotEqual(
            Table([[1, 2], [3, 4]]),
            Table([[1, 2], [4, 3]])
        )

    def test_head_all_rows(self: Self) -> None:
        table: Table = Table([[1], [2], [3]])
        self.assertEqual(table.head(3), table)

    def test_tail_all_row(self: Self) -> None:
        table: Table = Table([[1, 2], [3, 4], [5, 6]])
        self.assertEqual(table.tail(3), table)


    def test_head_zero_rows(self: Self) -> None:
        table: Table = Table([[1], [2], [3]])
        self.assertEqual(table.head(0), Table([]))

    def test_tail_zero_row(self: Self) -> None:
        table: Table = Table([[1, 2], [3, 4], [5, 6]])
        self.assertEqual(table.tail(0), Table([]))

    def test_select_columns_one_column(self: Self) -> None:
        table: Table = Table([[1, 2, 3], [4, 5, 6]])
        self.assertEqual(
            table.select_columns([1]),
            Table([[2], [5]])
        )

    def test_large_concat_rows(self: Self) -> None:
        t1: Table = Table([[i] for i in range(50)])
        t2: Table = Table([[i] for i in range(50, 100)])
        expected: Table = Table([[i] for i in range(100)])
        self.assertEqual(t1.concat_rows(t2), expected)

    def test_large_select_columns(self: Self) -> None:
        table: Table = Table([[i, i + 1, i + 2, i + 3] for i in range(100)])
        expected: Table = Table([[i, i + 2] for i in range(100)])
        self.assertEqual(table.select_columns([0, 2]), expected)


if __name__ == "__main__":
    unittest.main()