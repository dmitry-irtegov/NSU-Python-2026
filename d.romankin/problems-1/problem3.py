import unittest
from io import StringIO
from unittest.mock import patch

def collatz(num: int):
    
    if (num <= 0):
        return []
    while (num != 1):
        print(num, end="->")
        num = num // 2 if not (num%2) else 3 * num + 1
        
    print(num)


class TestOutput(unittest.TestCase):
    def test_collatz(self):
        with patch('sys.stdout', new=StringIO()) as mock_out:
            collatz(3)
            self.assertEqual(mock_out.getvalue(), "3->10->5->16->8->4->2->1\n")
            mock_out.truncate(0)
            mock_out.seek(0)
            collatz(7)
            self.assertEqual(mock_out.getvalue(), "7->22->11->34->17->52->26->13->40->20->10->5->16->8->4->2->1\n")
            mock_out.truncate(0)
            mock_out.seek(0)
            collatz(-4)
            self.assertEqual(mock_out.getvalue(), "")

if __name__ == '__main__':
    n = int(input("Enter a number: "))
    collatz(n)
    unittest.main()
    
    