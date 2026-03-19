#!/usr/bin/env python3

class Table:
    def __init__(self, data):
        self.data = data

    def head(self, n):
        return Table(self.data[:n])

    def tail(self, n):
        if n == 0:
            return Table([])
        return Table(self.data[-n:])

    def select_rows(self, indices):
        return Table([self.data[i] for i in indices])

    def select_cols(self, indices):
        if not indices:
            return Table([])
        return Table([[row[j] for j in indices] for row in self.data])

    def concat_rows(self, other):
        return Table(self.data + other.data)

    def concat_cols(self, other):
        return Table([row_self + row_other for row_self, row_other in zip(self.data, other.data)])

    def __str__(self):
        return '\n'.join('\t'.join(str(x) for x in row) for row in self.data)


def main():
    a = Table([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    b = Table([['a', 'b', 'c'], ['d', 'e', 'g'], ['f', 'k', 'm']])

    print("=== table a ===")
    print(a)

    print("\n=== table b ===")
    print(b)

    print("\n=== head(2) ===")
    print(a.head(2))

    print("\n=== tail(2) ===")
    print(a.tail(2))

    print("\n=== select_rows([0, 2]) ===")
    print(a.select_rows([0, 2]))

    print("\n=== select_cols([0, 2]) ===")
    print(a.select_cols([0, 2]))

    print("\n=== concat_rows ===")
    print(a.concat_rows(b))

    print("\n=== concat_cols ===")
    print(a.concat_cols(b))

if __name__ == "__main__":
    import sys

    try:
        main()
    except Exception as e:
        print(f"Unexpected error: {e}", file=sys.stderr)
        sys.exit(1)

