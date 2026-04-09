import problem4

import unittest
from io import StringIO
from unittest.mock import patch


class TestOutput(unittest.TestCase):
    
                             
    def test_example(self):
        with patch('sys.stdout', new=StringIO()) as mock_out:
            
            problem4.main("123")
            self.assertEqual(mock_out.getvalue(), 
                             """Found 4185 results.
Positions: 1923 2937 2975 3891 6547 ...\n""")
            
    def test_zero_index(self):
        with patch('sys.stdout', new=StringIO()) as mock_out:
            
            problem4.main("1415")
            self.assertEqual(mock_out.getvalue(), 
                             """Found 424 results.
Positions: 0 6954 29135 45233 79686 ...\n""")
            
    def test_less_than_five(self):
        with patch('sys.stdout', new=StringIO()) as mock_out:
            
            problem4.main("123456")
            self.assertEqual(mock_out.getvalue(), 
                             """Found 2 results.
Positions: 2458884 3735792\n""")
    
    def test_non_int_input(self):
        with patch('sys.stdout', new=StringIO()) as mock_out:
            
            problem4.main("string input")
            self.assertEqual(mock_out.getvalue(), 
                             """Found 0 results.\n""")

    def test_no_results(self):
            with patch('sys.stdout', new=StringIO()) as mock_out:
                
                problem4.main("1234091374676")
                self.assertEqual(mock_out.getvalue(), 
                                """Found 0 results.\n""")
                
    def test_pi(self):
            with patch('sys.stdout', new=StringIO()) as mock_out:
                
                problem4.main("3.14")
                self.assertEqual(mock_out.getvalue(), 
                                """Found 0 results.\n""")
if __name__ == '__main__':
    unittest.main()