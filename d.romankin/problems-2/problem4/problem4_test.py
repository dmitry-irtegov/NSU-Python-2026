import problem4

import unittest
from io import StringIO
from unittest.mock import patch


class TestOutput(unittest.TestCase):
    def test_pi(self):
        
        with patch('sys.stdout', new=StringIO()) as mock_out:
            seq1 = "123"
            seq2 = "1415"
            seq3 = "123456"
            problem4.main(seq1)
            self.assertEqual(mock_out.getvalue(), 
                             """Found 4185 results.
Positions: 1923 2937 2975 3891 6547 ...\n""")
            mock_out.truncate(0)
            mock_out.seek(0)
            problem4.main(seq2)
            self.assertEqual(mock_out.getvalue(), 
                             """Found 424 results.
Positions: 0 6954 29135 45233 79686 ...\n""")
            mock_out.truncate(0)
            mock_out.seek(0)
            problem4.main(seq3)
            self.assertEqual(mock_out.getvalue(), 
                             """Found 2 results.
Positions: 2458884 3735792\n""")
            mock_out.truncate(0)
            mock_out.seek(0)
            problem4.main("string input")
            self.assertEqual(mock_out.getvalue(), 
                             """Found 0 results.\n""")


if __name__ == '__main__':
    unittest.main()