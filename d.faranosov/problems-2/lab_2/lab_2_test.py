import unittest
from lab_2 import convert_dict_from_file, get_dict_from_file, convert_dict
import dict_generator


class MyTestCase(unittest.TestCase):
    def test_simple(self):
        converted_dict = convert_dict_from_file("simple.txt")
        ans = [('baca', ['fruit']),
               ('bacca', ['fruit']),
               ('malum', ['apple', 'punishment']),
               ('multa', ['punishment']),
               ('pomum', ['apple']),
               ('popula', ['apple']),
               ('popum', ['fruit'])]
        self.assertEqual(converted_dict, ans)

    def test_hard(self):
        file_dict = get_dict_from_file("hard.txt")
        converted_dict = convert_dict(file_dict)
        last_word = ""
        for (key, values) in converted_dict:
            if last_word != "":
                self.assertTrue(key >= last_word)
            last_word = key
            last_value = ""
            for value in values:
                if last_value != "":
                    self.assertTrue(last_value <= value)
                last_value = value
                self.assertTrue(key in file_dict[value])


if __name__ == '__main__':
    unittest.main()
