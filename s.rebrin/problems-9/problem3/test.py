import unittest
from main import Directory


class TestDirectory(unittest.TestCase):
    def test_no_calls_initially(self):
        d = Directory()
        self.assertEqual(str(d), "{}")

    def test_single_method_call(self):
        class A(Directory):
            def foo(self, x):
                return x * 2

        a = A()
        res = a.foo(5)

        self.assertEqual(res, 10)

        log = a.__dict__["m"]
        self.assertIn("foo", log)
        self.assertEqual(log["foo"]["count"], 1)
        self.assertEqual(log["foo"]["calls"][0]["args"], (5,))
        self.assertEqual(log["foo"]["calls"][0]["kwargs"], {})

    def test_multiple_calls(self):
        class A(Directory):
            def foo(self, x):
                return x

        a = A()
        a.foo(1)
        a.foo(2)
        a.foo(3)

        log = a.__dict__["m"]
        self.assertEqual(log["foo"]["count"], 3)

        args_list = [call["args"][0] for call in log["foo"]["calls"]]
        self.assertEqual(args_list, [1, 2, 3])

    def test_kwargs(self):
        class A(Directory):
            def foo(self, x=0):
                return x

        a = A()
        a.foo(x=10)

        log = a.__dict__["m"]
        self.assertEqual(log["foo"]["calls"][0]["kwargs"], {"x": 10})

    def test_multiple_methods(self):
        class A(Directory):
            def foo(self):
                return "foo"

            def bar(self):
                return "bar"

        a = A()
        a.foo()
        a.bar()

        log = a.__dict__["m"]
        self.assertIn("foo", log)
        self.assertIn("bar", log)

    def test_inheritance(self):
        class A(Directory):
            def add(self, x, y):
                return x + y

        a = A()
        result = a.add(2, 3)

        self.assertEqual(result, 5)

        log = a.__dict__["m"]
        self.assertEqual(log["add"]["count"], 1)

    def test_str_output(self):
        class A(Directory):
            def foo(self):
                pass

        a = A()
        a.foo()

        s = str(a)
        self.assertIn("foo", s)
        self.assertIn("count", s)

    def test_non_callable_attribute(self):
        class A(Directory):
            def __init__(self):
                self.x = 10

        a = A()
        self.assertEqual(a.x, 10)


if __name__ == "__main__":
    unittest.main()
