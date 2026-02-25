import unittest
from lab_3 import set_files

class MyTestCase(unittest.TestCase):
    def test(self):
        listed_files = set_files(".\\test_dir")
        self.assertEqual(len(listed_files), 3)
        ans = {
            ".\\test_dir\\a": 9,
            ".\\test_dir\\d": 7,
            ".\\test_dir\\c": 7
        }
        for (key, value) in listed_files:
            self.assertEqual(value, ans[key])


if __name__ == '__main__':
    unittest.main()
