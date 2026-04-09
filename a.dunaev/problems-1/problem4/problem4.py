#!/usr/bin/python

NUMS = ["no", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"]


def sing_song() -> None:
    for n in range(10, 0, -1):
        current_bottles = "bottle" if n == 1 else "bottles"
        next_bottles = "bottle" if n - 1 == 1 else "bottles"
        print(
            f"{NUMS[n].capitalize()} green {current_bottles} sitting on the wall,\n"
            f"{NUMS[n].capitalize()} green {current_bottles} sitting on the wall,\n"
            "And if one green bottle should accidentally fall,\n"
            f"There’ll be {NUMS[n - 1]} green {next_bottles} sitting on the wall.\n",
            end="",
        )
        if n > 1:
            print()


def main() -> None:
    sing_song()


if __name__ == "__main__":
    main()
