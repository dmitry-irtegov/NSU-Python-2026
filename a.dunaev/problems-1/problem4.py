#!/usr/bin/python
nums = ["no", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"]
n = 10
while n != 0:
    print(f"{nums[n].capitalize()} green bottles sitting on the wall,\n" * 2 +
          "And if one green bottle should accidentally fall,\n" +
          f"There’ll be {nums[n-1]} green bottles sitting on the wall.\n")
    n -= 1