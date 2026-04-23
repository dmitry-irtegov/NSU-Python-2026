import problem3

import unittest

from io import StringIO
from unittest.mock import patch
import importlib


class TestFiles(unittest.TestCase):


    def test_files(self):
        with patch('sys.stdout', new=StringIO()) as mock_out:
            problem3.main("test")
            
            mock_print = mock_out.getvalue()
            
            self.assertEqual(mock_print,  """test/_schneine 49
test/_pepe 37
test/_qwerty 37
test/ab 10
test/b 7
test/abcdef 3
test/a 1
test/y 1
test/z 1
test/a_zero 0
test/zero 0
""")
    
    def test_same_size(self):
        with patch('sys.stdout', new=StringIO()) as mock_out:
            problem3.main("same_size")
            
            mock_print = mock_out.getvalue()
            
            self.assertEqual(mock_print,  """same_size/$ 1000
same_size/1 1000
same_size/_ 1000
same_size/a 1000
same_size/b 1000
same_size/c 1000
same_size/z 1000
""")
            
    def test_subdir(self):
        with patch('sys.stdout', new=StringIO()) as mock_out:
            problem3.main("subdir")
            
            mock_print = mock_out.getvalue()
            self.assertEqual(mock_print,  """subdir/$ 1000
subdir/1 1000
subdir/_ 1000
subdir/a 1000
subdir/b 1000
subdir/c 1000
subdir/z 1000
""")
    
    def test_zeroes(self):
        with patch('sys.stdout', new=StringIO()) as mock_out:
            problem3.main("zeroes")
            
            mock_print = mock_out.getvalue()
            
            self.assertEqual(mock_print,  """zeroes/$ 0
zeroes/1 0
zeroes/_ 0
zeroes/a 0
zeroes/b 0
zeroes/c 0
zeroes/z 0
""")
            

    def test_not_a_directory(self):

        with patch('sys.stdout', new=StringIO()) as mock_out,\
            patch('sys.stderr', new=StringIO()) as mock_err:
            importlib.reload(problem3)
            problem3.main("problem3_test.py")
            mock_print = mock_out.getvalue()
            mock_err_print = mock_err.getvalue()
            self.assertEqual(mock_print,  """""")
            self.assertEqual(mock_err_print,  """Wrong path - problem3_test.py not a directory\n""")
    
    def test_empty_path(self):

        with patch('sys.stdout', new=StringIO()) as mock_out,\
            patch('sys.stderr', new=StringIO()) as mock_err:
            importlib.reload(problem3)
            problem3.main("")
            mock_print = mock_out.getvalue()
            mock_err_print = mock_err.getvalue()
            self.assertEqual(mock_print,  """""")
            self.assertEqual(mock_err_print,  """Wrong path -  not a directory\n""")
    
    
            


if __name__ == '__main__':
    unittest.main()