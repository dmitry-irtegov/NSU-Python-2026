import problem2

import unittest
from io import StringIO
from unittest.mock import patch
from sys import stderr
from os import remove

class TestOutput(unittest.TestCase):
    def test_dict(self):
        
        with patch('sys.stdout', new=StringIO()) as mock_out:
            problem2.main("problem2.txt")
            self.assertEqual(mock_out.getvalue().strip(), 
"""baca - fruit
bacca - fruit
malum - apple, punishment
multa - punishment
pomum - apple
popula - apple
popum - fruit""")
            filename_rev = "problem2_reversed.txt"
            try:
                rev_file = open("problem2_reversed.txt", 'w')
            except OSError as err:
                print("Cannot open the file", err, file=stderr)
                return
            rev_file.write(mock_out.getvalue())
            rev_file.close()
            mock_out.truncate(0)
            mock_out.seek(0)
            problem2.main(filename_rev)
            try:
                remove(filename_rev)
            except OSError as err:
                print("Error during file removing ", err, file=stderr)
                return
            self.assertEqual(mock_out.getvalue().strip(), 
"""apple - malum, pomum, popula
fruit - baca, bacca, popum
punishment - malum, multa""")


if __name__ == '__main__':

    unittest.main()
    