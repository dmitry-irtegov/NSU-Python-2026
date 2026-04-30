from collections.abc import Iterable
from typing import Self

TableValue = object


class Table:
    def __init__(self, rows: Iterable[Iterable[TableValue]]) -> None:
        self._rows: tuple[tuple[TableValue, ...], ...] = tuple(
            tuple(row) for row in rows
        )

    def head(self, count: int) -> Self:
        return type(self)(self._rows[:count])

    def tail(self, count: int) -> Self:
        if count == 0:
            return type(self)(())

        return type(self)(self._rows[-count:])

    def rows(self, indices: Iterable[int]) -> Self:
        return type(self)(self._rows[index] for index in indices)

    def merge_rows(self, other: Self) -> Self:
        return type(self)(self._rows + other._rows)

    def merge_columns(self, other: Self) -> Self:
        return type(self)(
            (
                left_row + right_row
                for left_row, right_row in zip(self._rows, other._rows)
            )
        )

    def slice(self, column_indices: Iterable[int]) -> Self:
        selected_columns = tuple(column_indices)

        return type(self)(
            (
                tuple(row[column_index] for column_index in selected_columns)
                for row in self._rows
            )
        )

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Table):
            return False

        return self._rows == other._rows

    def __getitem__(self, index: int) -> tuple[TableValue, ...]:
        return self._rows[index]

    def __len__(self) -> int:
        return len(self._rows)

    def __str__(self) -> str:
        return "\n".join("\t".join(str(value) for value in row) for row in self._rows)
