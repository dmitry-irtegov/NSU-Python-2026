import problem3

import unittest
from io import StringIO
from unittest.mock import patch
from os import remove, mkdir, rmdir
from sys import stderr
import random
from string import ascii_letters, digits

class TestOutput(unittest.TestCase):
    def test_files(self):
        chars = ascii_letters + digits
        with patch('sys.stdout', new=StringIO()) as mock_out:
            random.seed(42)
            files_num = random.randint(1, 50)
            filenames = []
            for i in range(files_num):
                rand_str = ''.join(random.choices(chars, k=random.randint(1, 15)))
                filenames.append(rand_str)
            try:
                for i in filenames:
                    fp = open(i, 'w')
                    fp.write(''.join(random.choices(chars, k=random.randint(0, 500))))
                    fp.close()
            except OSError as err:
                error_index = i
                print("OSerror catched: ", err, file=stderr)
                
                try:
                    for i in range(error_index + 1):
                        remove(filenames[i])
                except OSError as rm_file_err:
                    print("Cannot remove file ", rm_file_err, file=stderr)
                    return
                return
            problem3.main("./")
            try:
                for i in filenames:
                    remove(i)
            except OSError as rm_file_err:
                print("Cannot remove file ", rm_file_err, file=stderr)
                return
            mock_spl = mock_out.getvalue().splitlines()
            res_names = []
            res_sizes = []
            for i in mock_spl:
                pair = i.split(" ")
                res_names.append(pair[0])
                res_sizes.append(int(pair[1].strip()))
            
            self.assertEqual(res_sizes, sorted(res_sizes, reverse=True))
    def test_same_size(self):
        chars = ascii_letters + digits
        with patch('sys.stdout', new=StringIO()) as mock_out:
            random.seed(42)
            files_num = random.randint(1, 50)
            dirname = "test"
            try:
                mkdir(dirname)
            except OSError as err:
                print("Failed to create a directory ", err, file=stderr)
                return
            filenames = []
            for i in range(files_num):
                rand_str = dirname + "/" + ''.join(random.choices(chars, k=random.randint(1, 15)))
                filenames.append(rand_str)
            fixed_size = random.randint(0, 500)
            error_index = 0
            try:
                for i in range(len(filenames)):
                    fp = open(filenames[i], 'w')
                    fp.write(''.join(random.choices(chars, k=fixed_size)))
                    fp.close()
            except OSError as err:
                error_index = i
                print("OSerror catched: ", err, file=stderr)
                for i in range(error_index + 1):
                    try:
                        remove(filenames[i])
                    except OSError as rm_file_err:
                        print("Cannot remove file ", rm_file_err, file=stderr)
                        return
                try:
                    rmdir(dirname)
                except OSError as rm_dir_err:
                    print("Cannot remove dir ", rm_dir_err, file=stderr)
                    return
                return
            problem3.main("./test")
            try:
                for i in filenames:
                    remove(i)
            except OSError as rm_file_err:
                print("Cannot remove file ", rm_file_err, file=stderr)
                return
            try:
                rmdir(dirname)
            except OSError as rm_dir_err:
                print("Cannot remove dir ", rm_dir_err, file=stderr)
                return
            mock_spl = mock_out.getvalue().splitlines()
            res_names = []
            res_sizes = []
            for i in mock_spl:
                pair = i.split(" ")
                res_names.append(pair[0])
                res_sizes.append(int(pair[1].strip()))
            for i in res_sizes:
                self.assertEqual(i, fixed_size)
            self.assertEqual(res_names, sorted(res_names))
    
            


if __name__ == '__main__':
    unittest.main()
