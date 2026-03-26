#!/usr/bin/python
import unittest
import sys
from io import StringIO

def song():
    part1 = "green bottle" 
    part2 = " hanging on the wall"
    nums = [
        "Ten", "Nine", "Eight", "Seven", "Six", "Five", 
        "Four", "Three", "Two", "One", "no"
    ]
    
    for i in range(len(nums) - 1):
        current_s = "" if i == 9 else "s"
        s = f"{nums[i]} {part1}{current_s}{part2},"
        print(f"{s}\n{s}")
        print(f"And if {'that' if i == 9 else 'one'} green bottle should accidentally fall,")
        lower_num = nums[i + 1].lower()
        print(f"There'll be {lower_num} {part1}{'' if lower_num == 'one' else 's'}{part2}.")


class TestSong(unittest.TestCase):

    def test_song(self):
        original_stdout = sys.stdout
        sys.stdout = StringIO()

        song()

        output = sys.stdout.getvalue()
        sys.stdout = original_stdout

        expected = """Ten green bottles hanging on the wall,
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
There'll be one green bottle hanging on the wall.
One green bottle hanging on the wall,
One green bottle hanging on the wall,
And if that green bottle should accidentally fall,
There'll be no green bottles hanging on the wall.
"""
        self.assertEqual(output, expected)


if __name__ == "__main__":
    unittest.main()
