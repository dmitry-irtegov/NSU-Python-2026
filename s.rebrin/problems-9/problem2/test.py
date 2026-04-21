import unittest
from main import Storage


class TestStorage(unittest.TestCase):
    def test_successful_commit(self):
        s = Storage()

        with s.edit() as se:
            se["a"] = 1
            se["b"] = 2

        self.assertEqual(s["a"], 1)
        self.assertEqual(s["b"], 2)

    def test_rollback_on_exception(self):
        s = Storage()

        try:
            with s.edit() as se:
                se["a"] = 1
                raise ValueError("fail")
        except ValueError:
            pass

        self.assertEqual(s.data, {})

    def test_partial_changes_not_saved(self):
        s = Storage()

        try:
            with s.edit() as se:
                se["a"] = 1
                se["b"] = 2
                raise RuntimeError()
        except RuntimeError:
            pass

        self.assertEqual(s.data, {})

    def test_read_inside_context(self):
        s = Storage()
        s.data["x"] = 10

        with s.edit() as se:
            self.assertEqual(se["x"], 10)

    def test_overwrite_value(self):
        s = Storage()
        s.data["a"] = 1

        with s.edit() as se:
            se["a"] = 100

        self.assertEqual(s["a"], 100)

    def test_nested_dict_copy(self):
        s = Storage()
        s.data["a"] = {"inner": 1}

        with s.edit() as se:
            se["a"]["inner"] = 999

        self.assertEqual(s["a"]["inner"], 999)

    def test_multiple_transactions(self):
        s = Storage()

        with s.edit() as se:
            se["a"] = 1

        with s.edit() as se:
            se["b"] = 2

        self.assertEqual(s["a"], 1)
        self.assertEqual(s["b"], 2)

    def test_exception_does_not_break_future_transactions(self):
        s = Storage()

        try:
            with s.edit() as se:
                se["a"] = 1
                raise Exception()
        except Exception:
            pass

        with s.edit() as se:
            se["b"] = 2

        self.assertEqual(s.data, {"b": 2})

    def test_getitem_outside(self):
        s = Storage()
        s.data["x"] = 42

        self.assertEqual(s["x"], 42)

    def test_key_error(self):
        s = Storage()

        with self.assertRaises(KeyError):
            _ = s["missing"]


if __name__ == "__main__":
    unittest.main()
