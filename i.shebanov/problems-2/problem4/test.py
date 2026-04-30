import problem4
import unittest
from io import StringIO
from unittest.mock import patch


class TestOutput(unittest.TestCase):
    
    def test_example(self):
        with patch('sys.stdout', new=StringIO()) as mock_out:
            problem4.main("123")
            
            expected = (
                "Found 4185 results.\n"
                "Positions: 1923 2937 2975 3891 6547...\n"
            )
            self.assertEqual(mock_out.getvalue(), expected)
            
    def test_zero_index(self):
        with patch('sys.stdout', new=StringIO()) as mock_out:
            problem4.main("1415")
            
            expected = (
                "Found 424 results.\n"
                "Positions: 0 6954 29135 45233 79686...\n"
            )
            self.assertEqual(mock_out.getvalue(), expected)
            
    def test_less_than_five(self):
        with patch('sys.stdout', new=StringIO()) as mock_out:
            problem4.main("123456")
            
            expected = (
                "Found 2 results.\n"
                "Positions: 2458884 3735792\n"
            )
            self.assertEqual(mock_out.getvalue(), expected)
    
    def test_non_int_input(self):
        with patch('sys.stdout', new=StringIO()) as mock_out:
            problem4.main("string input")
            
            expected = "Found 0 results.\n"
            self.assertEqual(mock_out.getvalue(), expected)

    def test_no_results(self):
        with patch('sys.stdout', new=StringIO()) as mock_out:
            problem4.main("1234091374676")
            
            expected = "Found 0 results.\n"
            self.assertEqual(mock_out.getvalue(), expected)


if __name__ == '__main__':
    unittest.main()