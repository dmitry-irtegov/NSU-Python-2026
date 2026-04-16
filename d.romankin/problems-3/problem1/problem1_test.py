from problem1 import Table

import unittest


class TestTable(unittest.TestCase):
    def setUp(self):
        self.data = [
            [1, "A", 10.5],
            [2, "B", 20.0],
            [3, "C", 30.5],
            [4, "D", 40.0]
        ]
        self.table = Table(self.data)

    def test_head(self):
        result = self.table.head(2)
        self.assertEqual(len(result.data), 2)
        self.assertEqual(result.data[0], [1, "A", 10.5])
        self.assertEqual(result.data[1], [2, "B", 20.0])

    def test_tail(self):
        result = self.table.tail(2)
        self.assertEqual(len(result.data), 2)
        self.assertEqual(result.data[0], [3, "C", 30.5])
        self.assertEqual(result.data[-1], [4, "D", 40.0])

    def test_get_rows_by_indices(self):
        result = self.table.get_rows_by_indices([0, 3])
        self.assertEqual(len(result.data), 2)
        self.assertEqual(result.data[0], [1, "A", 10.5])
        self.assertEqual(result.data[1], [4, "D", 40.0])

    def test_concat_rows(self):
        other_data = [[5, "E", 50.0]]
        other_table = Table(other_data)
        
        combined = self.table.concat_rows(other_table)
        self.assertEqual(len(combined.data), 5)
        self.assertEqual(combined.data[-1], [5, "E", 50.0])

    def test_concat_cols(self):
        other_data = [["Yes"], ["No"], ["Yes"], ["No"]]
        other_table = Table(other_data)
        
        combined = self.table.concat_cols(other_table)
        self.assertEqual(len(combined.data), 4)
        self.assertEqual(len(combined.data[0]), 4)
        self.assertEqual(combined.data[0][-1], "Yes")


    def test_select_columns(self):
        result = self.table.select_columns([0, 2])
        self.assertEqual(len(result.data[0]), 2)
        self.assertEqual(result.data[0], [1, 10.5])
        self.assertEqual(result.data[2], [3, 30.5])

    def test_not_a_ref(self):
        new_table = Table(self.data)
        self.data[0][0] = 999
        self.assertNotEqual(new_table.data[0][0], 999)
        self.assertNotEqual(self.table.data[0][0], 999)


    def test_invalid_indices(self):
        with self.assertRaises(IndexError):
            self.table.get_rows_by_indices([99])
            
        with self.assertRaises(IndexError):
            self.table.select_columns([10])

    def test_immutability(self):
        t1 = Table([[1, "A", 1.5]])
        t2 = Table([[2, "B", 2.6]])
        combined = t1.concat_rows(t2)
           
        self.assertEqual(t1.data, [[1, "A", 1.5]])
        self.assertEqual(t2.data, [[2, "B", 2.6]])
        self.assertEqual(combined.data, [[1, "A", 1.5], [2, "B", 2.6]])

if __name__ == '__main__':
    unittest.main()