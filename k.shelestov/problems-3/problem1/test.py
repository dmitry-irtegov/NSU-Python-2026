from table import Table
import unittest


class TestTable(unittest.TestCase):

    def setUp(self):
        self.data = [
            [10, "X", 3.14],
            [20, "Y", 2.71],
            [30, "Z", 1.41],
            [40, "W", 0.99]
        ]
        self.table = Table(self.data)

    def test_head(self):
        result = self.table.head(2)
        self.assertEqual(len(result.data), 2)
        self.assertEqual(result.data[0], [10, "X", 3.14])
        self.assertEqual(result.data[1], [20, "Y", 2.71])

    def test_tail(self):
        result = self.table.tail(2)
        self.assertEqual(len(result.data), 2)
        self.assertEqual(result.data[0], [30, "Z", 1.41])
        self.assertEqual(result.data[1], [40, "W", 0.99])

    def test_select_rows(self):
        result = self.table.select_rows([1, 3])
        self.assertEqual(len(result.data), 2)
        self.assertEqual(result.data[0], [20, "Y", 2.71])
        self.assertEqual(result.data[1], [40, "W", 0.99])

    def test_select_columns(self):
        result = self.table.select_columns([0, 1])
        self.assertEqual(len(result.data), 4)
        self.assertEqual(result.data[0], [10, "X"])
        self.assertEqual(result.data[2], [30, "Z"])

    def test_concat_rows(self):
        other_table = Table([[50, "Q", 9.81]])

        combined = self.table.concat_rows(other_table)

        self.assertEqual(len(combined.data), 5)
        self.assertEqual(combined.data[-1], [50, "Q", 9.81])

    def test_concat_columns(self):
        other_table = Table([
            ["A"],
            ["B"],
            ["C"],
            ["D"]
        ])

        combined = self.table.concat_columns(other_table)

        self.assertEqual(len(combined.data), 4)
        self.assertEqual(len(combined.data[0]), 4)
        self.assertEqual(combined.data[0][-1], "A")
        self.assertEqual(combined.data[2][-1], "C")

    def test_deepcopy_safety(self):
        new_table = Table(self.data)

        self.data[0][1] = "CHANGED"

        self.assertNotEqual(new_table.data[0][1], "CHANGED")
        self.assertNotEqual(self.table.data[0][1], "CHANGED")

    def test_immutability(self):
        t1 = Table([[1, "A", 1.1]])
        t2 = Table([[2, "B", 2.2]])

        combined = t1.concat_rows(t2)

        self.assertEqual(t1.data, [[1, "A", 1.1]])
        self.assertEqual(t2.data, [[2, "B", 2.2]])
        self.assertEqual(combined.data, [[1, "A", 1.1], [2, "B", 2.2]])


if __name__ == "__main__":
    unittest.main()