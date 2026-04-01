#!/usr/bin/env python3


def song():
    nums = ["Ten", "Nine", "Eight", "Seven", "Six", "Five", "Four", "Three", "Two", "One", "No"]
    strs = ["green bottle", "hanging on the wall"]
    for i in range(len(nums) - 1):
        s = f"{nums[i]} {strs[0]}{'' if i == 9 else 's'} {strs[1]},"
        print(f"{s}\n{s}")
        print(f"{'If that' if i == 9 else 'And if'} one {strs[0]} should accidentally fall{'' if i == 9 else ','}")
        print(f"There’ll be {nums[i + 1].lower()} {strs[0]}{'' if i == 8 else 's'} {strs[1]}.")


if __name__ == "__main__":
    song()
