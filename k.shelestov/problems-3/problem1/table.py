from copy import deepcopy

class Table:
    def __init__(self, data):
        self.data = deepcopy(data)

    def __repr__(self):
        return "\n".join(map(str, self.data))

    def head(self, n):
        return Table(self.data[:n])

    def tail(self, n):
        return Table(self.data[-n:])

    def select_rows(self, indices):
        return Table([self.data[i] for i in indices])

    def select_columns(self, indices):
        return Table([[row[i] for i in indices] for row in self.data])

    def concat_rows(self, other):
        return Table(self.data + other.data)

    def concat_columns(self, other):
        return Table([self.data[i] + other.data[i] for i in range(len(self.data))])