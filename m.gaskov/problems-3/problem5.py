import unittest
from typing import Iterable, Self


class Table:
    """
    Store tabular data as immutable rows.

    A table is represented as a sequence of rows. Each row is converted to
    a tuple, and the whole table is stored as a tuple of rows. Methods that
    select or combine data return a new table and do not modify the original
    one.

    Parameters
    ----------
    rows : Iterable[Iterable[object]]
        Rows used to create the table. Each inner iterable represents one
        row of values.

    Attributes
    ----------
    _rows : tuple[tuple[object, ...], ...]
        Internal immutable representation of the table rows.

    Methods
    -------
    head(n)
        Return the first `n` rows.
    tail(n)
        Return the last `n` rows.
    select_rows(indices)
        Return rows selected by their indices.
    concat_rows(other)
        Concatenate two tables by rows.
    concat_columns(other)
        Concatenate two tables by columns.
    select_columns(indices)
        Return columns selected by their indices.

    Notes
    -----
    The table does not check that all rows have the same length. Operations
    that use indices may raise `IndexError` if an index is out of range.

    Examples
    --------
    >>> table = Table(((1, 2), (3, 4), (5, 6)))
    >>> table.head(2) == Table(((1, 2), (3, 4)))
    True
    >>> table.select_columns((0,)) == Table(((1,), (3,), (5,)))
    True
    """

    _rows: tuple[tuple[object, ...], ...]

    def __init__(self, rows: Iterable[Iterable[object]]) -> None:
        self._rows = tuple(tuple(row) for row in rows)

    def head(self: Self, n: int) -> Self:
        """
        Return the first `n` rows.

        Parameters
        ----------
        n : int
            Number of rows to take from the beginning of the table.

        Returns
        -------
        Table
            New table containing the first `n` rows.
        """
        return type(self)(self._rows[:n])

    def tail(self: Self, n: int) -> Self:
        """
        Return the last `n` rows.

        Parameters
        ----------
        n : int
            Number of rows to take from the end of the table.

        Returns
        -------
        Table
            New table containing the last `n` rows. If `n` is zero,
            an empty table is returned.
        """
        if n == 0:
            return type(self)(())
        return type(self)(self._rows[-n:])

    def select_rows(self: Self, indices: Iterable[int]) -> Self:
        """
        Return rows selected by indices.

        Parameters
        ----------
        indices : Iterable[int]
            Indices of rows to include in the result.

        Returns
        -------
        Table
            New table containing the selected rows in the given order.
        """
        return type(self)(self._rows[i] for i in indices)

    def concat_rows(self: Self, other: Self) -> Self:
        """
        Concatenate two tables by rows.

        Parameters
        ----------
        other : Table
            Table whose rows are added after the rows of the current table.

        Returns
        -------
        Table
            New table containing rows from both tables.
        """
        return type(self)(self._rows + other._rows)

    def concat_columns(self: Self, other: Self) -> Self:
        """
        Concatenate two tables by columns.

        Corresponding rows of both tables are joined together. The resulting
        table contains as many rows as the shorter input table.

        Parameters
        ----------
        other : Table
            Table whose columns are added to the right of the current table.

        Returns
        -------
        Table
            New table with rows formed by joining corresponding rows.
        """
        return type(self)(row1 + row2 for row1, row2 in zip(self._rows, other._rows))

    def select_columns(self: Self, indices: Iterable[int]) -> Self:
        """
        Return columns selected by indices.

        Parameters
        ----------
        indices : Iterable[int]
            Indices of columns to include in the result.

        Returns
        -------
        Table
            New table containing only the selected columns.
        """
        return type(self)((row[i] for i in indices) for row in self._rows)

    def __eq__(self: Self, other: object) -> bool:
        """
        Compare the table with another object.

        Two tables are equal if the other object is also a `Table` and both
        tables contain exactly the same rows.

        Parameters
        ----------
        other : object
            Object to compare with the current table.

        Returns
        -------
        bool
            `True` if both objects are equal tables, otherwise `False`.
        """
        if not isinstance(other, Table):
            return False
        return self._rows == other._rows


class TestTable(unittest.TestCase):
    """
    Unit tests for the `Table` class.

    This test case checks row selection, column selection, row and column
    concatenation, equality comparison, and table creation from different
    iterable objects.

    Methods
    -------
    test_head()
        Test selecting the first rows of a table.
    test_tail()
        Test selecting the last rows of a table.
    test_select_rows()
        Test selecting rows by indices.
    test_concat_rows()
        Test concatenating two tables by rows.
    test_concat_columns()
        Test concatenating two tables by columns.
    test_select_columns()
        Test selecting columns by indices.
    test_equality()
        Test equality comparison between tables.
    test_equality_with_non_table()
        Test comparison between a table and a non-table object.
    test_head_all_rows()
        Test selecting all rows from the beginning.
    test_tail_all_rows()
        Test selecting all rows from the end.
    test_tail_zero_rows()
        Test selecting zero rows from the end.
    test_select_columns_one_column()
        Test selecting a single column.
    test_large_sequence_concat_rows()
        Test row concatenation with larger tables.
    test_large_sequence_select_columns()
        Test column selection with a larger table.
    test_create_from_iterator()
        Test creating a table from an iterator.
    test_create_from_lazy_iterator()
        Test creating a table from a lazy row generator.
    """
    def test_head(self: Self) -> None:
        """
        Test that `head` returns the first requested rows.
        """
        table: Table = Table(((1, 2), (3, 4), (5, 6)))
        self.assertEqual(table.head(2), Table(((1, 2), (3, 4))))

    def test_tail(self: Self) -> None:
        """
        Test that `tail` returns the last requested rows.
        """
        table: Table = Table(((1, 2), (3, 4), (5, 6)))
        self.assertEqual(table.tail(2), Table(((3, 4), (5, 6))))

    def test_select_rows(self: Self) -> None:
        """
        Test selecting rows by their indices.
        """
        table: Table = Table(((10, 20), (30, 40), (50, 60)))
        self.assertEqual(table.select_rows((0, 2)), Table(((10, 20), (50, 60))))

    def test_concat_rows(self: Self) -> None:
        """
        Test concatenating two tables by rows.
        """
        t1: Table = Table(((1, 2), (3, 4)))
        t2: Table = Table(((5, 6), (7, 8)))
        self.assertEqual(
            t1.concat_rows(t2),
            Table(((1, 2), (3, 4), (5, 6), (7, 8)))
        )

    def test_concat_columns(self: Self) -> None:
        """
        Test concatenating two tables by columns.
        """
        t1: Table = Table(((1, 2), (3, 4)))
        t2: Table = Table(((5, 6), (7, 8)))
        self.assertEqual(
            t1.concat_columns(t2),
            Table((
                (1, 2, 5, 6),
                (3, 4, 7, 8)
            ))
        )

    def test_select_columns(self: Self) -> None:
        """
        Test selecting several columns by their indices.
        """
        table: Table = Table((
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

    def test_equality(self: Self) -> None:
        """
        Test equality and inequality between two tables.
        """
        self.assertEqual(
            Table(((1, 2), (3, 4))),
            Table(((1, 2), (3, 4)))
        )
        self.assertNotEqual(
            Table(((1, 2), (3, 4))),
            Table(((1, 2), (4, 3)))
        )

    def test_equality_with_non_table(self: Self) -> None:
        """
        Test that a table is not equal to a non-table object.
        """
        self.assertNotEqual(Table(((1, 2),)), ((1, 2),))

    def test_head_all_rows(self: Self) -> None:
        """
        Test that `head` can return all rows of a table.
        """
        table: Table = Table(((1,), (2,), (3,)))
        self.assertEqual(table.head(3), table)

    def test_tail_all_rows(self: Self) -> None:
        """
        Test that `tail` can return all rows of a table.
        """
        table: Table = Table(((1, 2), (3, 4), (5, 6)))
        self.assertEqual(table.tail(3), table)

    def test_tail_zero_rows(self: Self) -> None:
        """
        Test that `tail(0)` returns an empty table.
        """
        table: Table = Table(((1, 2), (3, 4), (5, 6)))
        self.assertEqual(table.tail(0), Table(()))

    def test_select_columns_one_column(self: Self) -> None:
        """
        Test selecting exactly one column.
        """
        table: Table = Table(((1, 2, 3), (4, 5, 6)))
        self.assertEqual(
            table.select_columns((1,)),
            Table(((2,), (5,)))
        )

    def test_large_sequence_concat_rows(self: Self) -> None:
        """
        Test row concatenation with larger generated tables.
        """
        t1: Table = Table((i,) for i in range(50))
        t2: Table = Table((i,) for i in range(50, 100))
        expected: Table = Table((i,) for i in range(100))
        self.assertEqual(t1.concat_rows(t2), expected)

    def test_large_sequence_select_columns(self: Self) -> None:
        """
        Test column selection with a larger generated table.
        """
        table: Table = Table(range(i, i + 4) for i in range(100))
        expected: Table = Table((i, i + 2) for i in range(100))
        self.assertEqual(table.select_columns((0, 2)), expected)

    def test_create_from_iterator(self: Self) -> None:
        """
        Test creating a table from an iterator of rows.
        """
        rows: Iterable[tuple[int, int]] = ((i, i + 1) for i in range(3))
        table: Table = Table(rows)
        self.assertEqual(
            table,
            Table(((0, 1), (1, 2), (2, 3)))
        )

    def test_create_from_lazy_iterator(self: Self) -> None:
        """
        Test creating a table from a lazy row generator.
        """
        def row_generator() -> Iterable[list[object]]:
            for i in range(3):
                yield [i, i + 1]

        table: Table = Table(row_generator())
        self.assertEqual(
            table,
            Table(((0, 1), (1, 2), (2, 3)))
        )


if __name__ == "__main__":
    unittest.main()
