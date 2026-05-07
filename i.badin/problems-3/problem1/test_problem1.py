from collections.abc import Iterator
import unittest

from problem1 import Table


class TableTests(unittest.TestCase):
    def test_table_can_be_created_from_tuple_rows(self) -> None:
        table: Table = Table(
            (
                ("Alice", 20),
                ("Bob", 21),
            )
        )

        self.assertEqual(table, Table([["Alice", 20], ["Bob", 21]]))

    def test_table_can_be_created_from_lazy_iterator(self) -> None:
        rows: Iterator[tuple[str, int]] = ((name, age) for name, age in (("Alice", 20), ("Bob", 21)))

        self.assertEqual(Table(rows), Table([["Alice", 20], ["Bob", 21]]))

    def test_head_returns_first_rows(self) -> None:
        table: Table = Table(
            [
                ["Alice", 20],
                ["Bob", 21],
                ["Charlie", 22],
            ]
        )

        self.assertEqual(
            table.head(2),
            Table(
                [
                    ["Alice", 20],
                    ["Bob", 21],
                ]
            ),
        )

    def test_tail_returns_last_rows(self) -> None:
        table = Table(
            [
                ["Alice", 20],
                ["Bob", 21],
                ["Charlie", 22],
            ]
        )

        self.assertEqual(
            table.tail(2),
            Table(
                [
                    ["Bob", 21],
                    ["Charlie", 22],
                ]
            ),
        )

    def test_tail_zero_returns_empty_table(self) -> None:
        self.assertEqual(Table([[1], [2], [3]]).tail(0), Table([]))

    def test_rows_returns_rows_by_indices(self) -> None:
        table: Table = Table(
            [
                ["Alice", 20],
                ["Bob", 21],
                ["Charlie", 22],
            ]
        )

        self.assertEqual(
            table.rows(index for index in [2, 0]),
            Table(
                [
                    ["Charlie", 22],
                    ["Alice", 20],
                ]
            ),
        )

    def test_merge_rows_appends_other_table_rows(self) -> None:
        first_table: Table = Table([["Alice", 20], ["Bob", 21]])
        second_table: Table = Table([["Charlie", 22], ["Dora", 23]])

        self.assertEqual(
            first_table.merge_rows(second_table),
            Table(
                [
                    ["Alice", 20],
                    ["Bob", 21],
                    ["Charlie", 22],
                    ["Dora", 23],
                ]
            ),
        )

    def test_merge_columns_appends_other_table_columns(self) -> None:
        first_table: Table = Table([["Alice", 20], ["Bob", 21]])
        second_table: Table = Table([["A"], ["B"]])

        self.assertEqual(
            first_table.merge_columns(second_table),
            Table(
                [
                    ["Alice", 20, "A"],
                    ["Bob", 21, "B"],
                ]
            ),
        )

    def test_slice_returns_selected_columns(self) -> None:
        table: Table = Table(
            [
                ["Alice", 20, "A"],
                ["Bob", 21, "B"],
            ]
        )

        self.assertEqual(
            table.slice(index for index in [2, 0]),
            Table(
                [
                    ["A", "Alice"],
                    ["B", "Bob"],
                ]
            ),
        )

    def test_getitem_returns_row_by_index(self) -> None:
        table: Table = Table([["Alice", 20], ["Bob", 21]])

        self.assertEqual(table[1], ("Bob", 21))

    def test_len_returns_number_of_rows(self) -> None:
        self.assertEqual(len(Table([[1], [2], [3]])), 3)

    def test_string_representation(self) -> None:
        table: Table = Table([["Alice", 20], ["Bob", 21]])

        self.assertEqual(str(table), "Alice\t20\nBob\t21")


if __name__ == "__main__":
    unittest.main()
