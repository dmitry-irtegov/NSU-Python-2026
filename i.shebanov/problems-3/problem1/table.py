class Table:
    def __init__(self, data=None):
        if data is None:
            self._rows = []
        else:
            self._rows = [list(row) for row in data]

    def head(self, n=5):
        return Table(self._rows[:n])

    def tail(self, n=5):
        if n == 0:
            return Table([])
        return Table(self._rows[-n:])

    def select_rows(self, indices):
        return Table([self._rows[i] for i in indices])

    def select_columns(self, indices):
        return Table([[row[i] for i in indices] for row in self._rows])

    def concat_rows(self, other):
        return Table(self._rows + other._rows)

    def concat_cols(self, other):
        return Table([a + b for a, b in zip(self._rows, other._rows)])

    def __eq__(self, other):
        if not isinstance(other, Table):
            return NotImplemented
        return self._rows == other._rows

    def __len__(self):
        return len(self._rows)

    def __getitem__(self, index):
        if isinstance(index, slice):
            return Table(self._rows[index])
        return list(self._rows[index])

    def __repr__(self):
        return "Table(" + repr(self._rows) + ")"
