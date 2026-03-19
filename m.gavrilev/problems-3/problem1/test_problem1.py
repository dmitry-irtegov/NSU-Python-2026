#!/usr/bin/env python3

import random
import unittest

from problem1 import Table


class TestHeadTail(unittest.TestCase):
    def test_head(self):
        t = Table([[1, 2], [3, 4], [5, 6]])
        self.assertEqual(t.head(2).data, [[1, 2], [3, 4]])

    def test_tail(self):
        t = Table([[1, 2], [3, 4], [5, 6]])
        self.assertEqual(t.tail(2).data, [[3, 4], [5, 6]])

    def test_zero(self):
        t = Table([[1, 2], [3, 4]])
        self.assertEqual(t.head(0).data, [])
        self.assertEqual(t.tail(0).data, [])

    def test_more_than_size(self):
        t = Table([[1, 2]])
        self.assertEqual(t.head(5).data, [[1, 2]])
        self.assertEqual(t.tail(5).data, [[1, 2]])

    def test_does_not_mutate(self):
        t = Table([[1, 2], [3, 4]])
        t.head(1)
        t.tail(1)
        self.assertEqual(t.data, [[1, 2], [3, 4]])

    def test_empty_table(self):
        t = Table([])
        self.assertEqual(t.head(0).data, [])
        self.assertEqual(t.head(5).data, [])
        self.assertEqual(t.tail(0).data, [])
        self.assertEqual(t.tail(5).data, [])


class TestSelect(unittest.TestCase):
    def test_rows(self):
        t = Table([[1, 2], [3, 4], [5, 6]])
        self.assertEqual(t.select_rows([1]).data, [[3, 4]])
        self.assertEqual(t.select_rows([0, 2]).data, [[1, 2], [5, 6]])

    def test_cols(self):
        t = Table([[1, 2, 3], [4, 5, 6]])
        self.assertEqual(t.select_cols([1]).data, [[2], [5]])
        self.assertEqual(t.select_cols([0, 2]).data, [[1, 3], [4, 6]])

    def test_reorder(self):
        t = Table([[1, 2, 3], [4, 5, 6]])
        self.assertEqual(t.select_rows([1, 0]).data, [[4, 5, 6], [1, 2, 3]])
        self.assertEqual(t.select_cols([2, 0]).data, [[3, 1], [6, 4]])

    def test_duplicate_index(self):
        t = Table([[1, 2], [3, 4]])
        self.assertEqual(t.select_rows([0, 0]).data, [[1, 2], [1, 2]])
        self.assertEqual(t.select_cols([1, 1]).data, [[2, 2], [4, 4]])

    def test_empty_indices(self):
        t = Table([[1, 2], [3, 4]])
        self.assertEqual(t.select_rows([]).data, [])
        self.assertEqual(t.select_cols([]).data, [])

    def test_empty_table(self):
        t = Table([])
        self.assertEqual(t.select_rows([]).data, [])
        self.assertEqual(t.select_cols([]).data, [])


class TestConcat(unittest.TestCase):
    def test_rows(self):
        a = Table([[1, 2], [3, 4]])
        b = Table([[5, 6]])
        self.assertEqual(a.concat_rows(b).data, [[1, 2], [3, 4], [5, 6]])

    def test_cols(self):
        a = Table([[1, 2], [3, 4]])
        b = Table([[5], [6]])
        self.assertEqual(a.concat_cols(b).data, [[1, 2, 5], [3, 4, 6]])

    def test_rows_with_empty(self):
        a = Table([[1, 2]])
        self.assertEqual(a.concat_rows(Table([])).data, [[1, 2]])
        self.assertEqual(Table([]).concat_rows(Table([])).data, [])

    def test_cols_with_empty(self):
        a = Table([[1, 2]])
        self.assertEqual(a.concat_cols(Table([])).data, [])
        self.assertEqual(Table([]).concat_cols(Table([])).data, [])

    # TODO: тут нужно raise ValueError из-за zip row удалилась но не упала
    def test_cols_different_row_count(self):
        a = Table([[1, 2], [3, 4], [5, 6]])
        b = Table([[7], [8]])
        result = a.concat_cols(b)
        self.assertEqual(result.data, [[1, 2, 7], [3, 4, 8]])

    # TODO: тут нужно raise ValueError из-за разной ширины строк
    def test_rows_different_col_count(self):
        a = Table([[1, 2], [3, 4]])
        b = Table([[5, 6, 7]])
        result = a.concat_rows(b)
        self.assertEqual(result.data, [[1, 2], [3, 4], [5, 6, 7]])

    def test_does_not_mutate(self):
        a = Table([[1, 2]])
        b = Table([[3, 4]])
        a.concat_rows(b)
        a.concat_cols(b)
        self.assertEqual(a.data, [[1, 2]])
        self.assertEqual(b.data, [[3, 4]])


class TestStr(unittest.TestCase):
    def test_format(self):
        self.assertEqual(str(Table([[1, 2, 3]])), "1\t2\t3")
        self.assertEqual(str(Table([[1, 2], [3, 4]])), "1\t2\n3\t4")
        self.assertEqual(str(Table([])), "")
        self.assertEqual(str(Table([[1, 'a'], ['b', 2]])), "1\ta\nb\t2")


def random_table(rng, rows, cols):
    data = [[rng.randint(-100, 100) for _ in range(cols)] for _ in range(rows)]
    return Table(data), data


class TestRandomInvariants(unittest.TestCase):
    def test_head_tail_cover_all_rows(self):
        rng = random.Random(1000)
        rows = rng.randint(3, 20)
        cols = rng.randint(2, 10)
        t, data = random_table(rng, rows, cols)
        n = rng.randint(1, rows - 1)
        self.assertEqual(t.head(n).data + t.tail(rows - n).data, data)

    def test_select_all_is_identity(self):
        rng = random.Random(1010)
        rows = rng.randint(3, 20)
        cols = rng.randint(2, 10)
        t, data = random_table(rng, rows, cols)
        self.assertEqual(t.select_rows(list(range(rows))).data, data)
        self.assertEqual(t.select_cols(list(range(cols))).data, data)

    def test_concat_rows_then_head_tail_roundtrip(self):
        rng = random.Random(3333)
        cols = rng.randint(2, 10)
        rows_a = rng.randint(2, 10)
        rows_b = rng.randint(2, 10)
        a, data_a = random_table(rng, rows_a, cols)
        b, data_b = random_table(rng, rows_b, cols)
        merged = a.concat_rows(b)
        self.assertEqual(merged.head(rows_a).data, data_a)
        self.assertEqual(merged.tail(rows_b).data, data_b)

    def test_concat_cols_then_select_cols_roundtrip(self):
        rng = random.Random(3232)
        rows = rng.randint(2, 10)
        cols_a = rng.randint(2, 5)
        cols_b = rng.randint(2, 5)
        a, data_a = random_table(rng, rows, cols_a)
        b, data_b = random_table(rng, rows, cols_b)
        merged = a.concat_cols(b)
        left = merged.select_cols(list(range(cols_a)))
        right = merged.select_cols(list(range(cols_a, cols_a + cols_b)))
        self.assertEqual(left.data, data_a)
        self.assertEqual(right.data, data_b)


if __name__ == "__main__":
    unittest.main()
