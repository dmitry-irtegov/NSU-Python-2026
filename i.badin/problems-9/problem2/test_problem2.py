import unittest

from problem2 import Storage


class StorageTestCase(unittest.TestCase):
    def test_successful_transaction_commits_changes(self):
        storage = Storage()

        with storage.edit() as editable:
            editable["a"] = 1
            editable["b"] = 2
            editable["a"] = 3

        self.assertEqual(3, storage["a"])
        self.assertEqual(2, storage["b"])

    def test_failed_transaction_rolls_back_changes(self):
        storage = Storage()

        with storage.edit() as editable:
            editable["a"] = 1

        with self.assertRaises(ValueError):
            with storage.edit() as editable:
                editable["a"] = 10
                editable["b"] = 20
                raise ValueError("error")

        self.assertEqual(1, storage["a"])
        with self.assertRaises(KeyError):
            _ = storage["b"]

    def test_nested_transaction_is_forbidden(self):
        storage = Storage()

        with storage.edit():
            with self.assertRaises(RuntimeError):
                storage.edit()

    def test_transaction_allows_deleting_keys(self):
        storage = Storage()

        with storage.edit() as editable:
            editable["a"] = 1

        with storage.edit() as editable:
            del editable["a"]

        with self.assertRaises(KeyError):
            _ = storage["a"]


if __name__ == "__main__":
    unittest.main()
