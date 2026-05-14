import unittest
from io import StringIO
import sys


def kollats(n):
    while n > 1:
        print(str(n) + "->", end='')
        n = n // 2 if n % 2 == 0 else 3 * n + 1
    print(1)
    

class TestKollatc(unittest.TestCase):

    def test_base(self):
        original_stdout = sys.stdout
        sys.stdout = StringIO()

        kollats(1)

        output = sys.stdout.getvalue()
        sys.stdout = original_stdout

        self.assertEqual(output, "1\n")

    def test_lt_1(self):
        original_stdout = sys.stdout
        sys.stdout = StringIO()

        kollats(-52)

        output = sys.stdout.getvalue()
        sys.stdout = original_stdout

        self.assertEqual(output, "1\n")

    def test_sixseven(self):
        original_stdout = sys.stdout
        sys.stdout = StringIO()

        kollats(67)

        output = sys.stdout.getvalue()
        sys.stdout = original_stdout

        expected = "67->202->101->304->152->76->38->19->58->29->88->44->22->11->34->17->52->26->13->40->20->10->5->16->8->4->2->1\n"
        self.assertEqual(output, expected)


if __name__ == "__main__":
    unittest.main()