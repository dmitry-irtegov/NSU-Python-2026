import unittest
from sortedDict import SortedDict, SortedDictNode, Color


class TestSortedDict(unittest.TestCase):
    def setUp(self) -> None:
        self.d : SortedDict[int, str] = SortedDict[int, str]()

    def _assert_red_black_properties(self) -> None:
        # свойство 1: корень чёрный
        self.assertEqual(self.d._root.color, Color.BLACK,
                         "Root must be black")

        # подсчет черной высоты
        def check(node : SortedDictNode[int, str]) -> int:
            if node == self.d._noneNode:
                return 1

            # свойство 2: красный узел не может иметь красных детей
            if node.color == Color.RED:
                self.assertTrue(node.leftChild is None or node.leftChild.color == Color.BLACK,
                                f"Red node {node.key} has red left child")
                self.assertTrue(node.rightChild is None or node.rightChild.color == Color.BLACK,
                                f"Red node {node.key} has red right child")

            assert node.leftChild is not None and node.rightChild is not None
            left_bh : int = check(node.leftChild)
            right_bh : int = check(node.rightChild)

            # свойство 3: одинаковая чёрная высота в обоих поддеревьях
            self.assertEqual(left_bh, right_bh,
                             f"Incorrect black height {node.key}")

            return left_bh + (1 if node.color == Color.BLACK else 0)

        _ = check(self.d._root)

    def test_insert_and_search(self) -> None:
        self.d[5] = "five"
        self.d[3] = "three"
        self.d[7] = "seven"

        self.assertEqual(self.d[5], "five")
        self.assertEqual(self.d[3], "three")
        self.assertEqual(self.d[7], "seven")

        self.assertTrue(5 in self.d)
        self.assertTrue(3 in self.d)
        self.assertTrue(7 in self.d)

        self.assertFalse(10 in self.d)
        self._assert_red_black_properties()

    def test_insert_duplicate_key_updates_value(self) -> None:
        self.d[1] = "old"
        self.d[1] = "new"
        self.assertEqual(self.d[1], "new")
        self._assert_red_black_properties()

    def test_getitem_key_error(self) -> None:
        with self.assertRaises(KeyError):
            _ = self.d[100]

    def test_delitem_basic(self) -> None:
        self.d[10] = "a"
        self.d[5] = "b"
        self.d[15] = "c"
        del self.d[5]

        self.assertFalse(5 in self.d)
        self.assertEqual(len(list(self.d.items())), 2)
        self._assert_red_black_properties()

    def test_delitem_key_error(self) -> None:
        with self.assertRaises(KeyError):
            del self.d[999]


    def test_delete_root(self) -> None:
        self.d[42] = "root"
        del self.d[42]
        self.assertFalse(42 in self.d)
        self.assertEqual(len(list(self.d.items())), 0)

        for k in [10, 5, 15, 3, 7]:
            self.d[k] = str(k)
        assert self.d._root.key is not None
        root_key : int = self.d._root.key
        del self.d[root_key]
        self.assertFalse(root_key in self.d)
        self._assert_red_black_properties()


    def test_iter_empty(self) -> None:
        self.assertEqual(list(self.d), [])
        self.assertEqual(list(self.d.items()), [])

    def test_iter_keys(self) -> None:
        keys : list[int] = [7, 2, 5, 1, 9]
        for k in keys:
            self.d[k] = str(k)
        self.assertEqual(list(self.d), [1, 2, 5, 7, 9])

    def test_iter_items(self) -> None:
        items : list[tuple[int, str]] = [(7, "a"), (2, "b"), (5, "c")]
        for k, v in items:
            self.d[k] = v
        expected : list[tuple[int, str]] = sorted(items)
        self.assertEqual(list(self.d.items()), expected)

    def test_insert_ascending_order(self) -> None:
        for i in range(1, 11):
            self.d[i] = str(i)
        self.assertEqual(list(self.d), list(range(1, 11)))
        self._assert_red_black_properties()

    def test_insert_descending_order(self) -> None:
        for i in range(10, 0, -1):
            self.d[i] = str(i)
        self.assertEqual(list(self.d), list(range(1, 11)))
        self._assert_red_black_properties()

    def test_init_from_dict(self) -> None:
        l : list[tuple[int, int]] = [(1, 1), (2, 2), (3, 3), (4, 4), (-1, -1), (-2, -2), (-3, -3)]
        sorted_dict : SortedDict[int, int] = SortedDict(l)
        l.sort(key=lambda x: x[0])
        self.assertEqual(list(sorted_dict.items()), l)

if __name__ == "__main__":
    unittest.main()