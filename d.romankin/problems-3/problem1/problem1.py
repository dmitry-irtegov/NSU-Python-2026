class Table:
    def __init__(self, data):
        
        self.data = [list(row) for row in data]

    def head(self, n):
        return Table(self.data[:n])

    def tail(self, n):
        if n == 0:
            return Table([])
        return Table(self.data[-n:])

    def get_rows_by_indices(self, indices):
        new_data = [self.data[i] for i in indices]
        return Table(new_data)

    def concat_rows(self, other):
        return Table(self.data + other.data)

    def concat_cols(self, other):
        new_data = [row_a + row_b for row_a, row_b in zip(self.data, other.data)]
        return Table(new_data)

    def select_columns(self, col_indices):
        new_data = []
        for row in self.data:
            new_row = [row[i] for i in col_indices]
            new_data.append(new_row)
        return Table(new_data)

    def __str__(self):
        return "\n".join([str(row) for row in self.data])
    