#!/usr/bin/env python3.12
import unittest
from unittest.mock import patch
import io
import sys

song = """Ten green bottles hanging on the wall,
Ten green bottles hanging on the wall,
And if one green bottle should accidentally fall,
There'll be nine green bottles hanging on the wall.

Nine green bottles hanging on the wall,
Nine green bottles hanging on the wall,
And if one green bottle should accidentally fall,
There'll be eight green bottles hanging on the wall.

Eight green bottles hanging on the wall,
Eight green bottles hanging on the wall,
And if one green bottle should accidentally fall,
There'll be seven green bottles hanging on the wall.

Seven green bottles hanging on the wall,
Seven green bottles hanging on the wall,
And if one green bottle should accidentally fall,
There'll be six green bottles hanging on the wall.

Six green bottles hanging on the wall,
Six green bottles hanging on the wall,
And if one green bottle should accidentally fall,
There'll be five green bottles hanging on the wall.

Five green bottles hanging on the wall,
Five green bottles hanging on the wall,
And if one green bottle should accidentally fall,
There'll be four green bottles hanging on the wall.

Four green bottles hanging on the wall,
Four green bottles hanging on the wall,
And if one green bottle should accidentally fall,
There'll be three green bottles hanging on the wall.

Three green bottles hanging on the wall,
Three green bottles hanging on the wall,
And if one green bottle should accidentally fall,
There'll be two green bottles hanging on the wall.

Two green bottles hanging on the wall,
Two green bottles hanging on the wall,
And if one green bottle should accidentally fall,
There'll be one green bottles hanging on the wall.

One green bottle hanging on the wall,
One green bottle hanging on the wall,
If that one green bottle should accidentally fall
There'll be no green bottle hanging on the wall.""" + "\n\n"

def tenGreenBottles():
    str_numbers = ['Ten', 'Nine', 'Eight', 'Seven', 'Six', 'Five', 'Four', 'Three', 'Two', 'One', 'No']

    first_line = ' green bottle{s} hanging on the wall,'
    third_line = '{} one green bottle should accidentally fall{}'
    fourth_line = ' green bottle{} hanging on the wall.'

    for i in range(10):
        print(str_numbers[i] + first_line.format(s = 's' if i != 9 else ''))
        print(str_numbers[i] + first_line.format(s = 's' if i != 9 else ''))
        print(third_line.format('And if' if i != 9 else 'If that', ',' if i != 9 else ''))
        print("There'll be " + str_numbers[i + 1].lower() + fourth_line.format('s' if i != 9 else '') + "\n")


class TestBottles(unittest.TestCase):
    def test_print_statement(self):
        with patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            tenGreenBottles()
            self.assertEqual(fake_stdout.getvalue(), song)

if __name__ == '__main__':
    tenGreenBottles()
    unittest.main()
    