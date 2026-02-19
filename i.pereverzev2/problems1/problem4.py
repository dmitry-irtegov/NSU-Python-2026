#!/usr/bin/python


def song():
    part = "green bottles hanging on the wall"
    nums = [
        "Ten",
        "Nine",
        "Eight",
        "Seven",
        "Six",
        "Five",
        "Four",
        "Three",
        "Two",
        "One",
        "no",
    ]
    for i in range(len(nums) - 1):
        s = f"{nums[i]} {part},"
        print(f"{s}\n{s}")
        print("And if one green bottle should accidentally fall,")
        lower_num = nums[i + 1].lower()
        print(f"There'll be {lower_num} {part}.")


if __name__ == "__main__":
    song()
