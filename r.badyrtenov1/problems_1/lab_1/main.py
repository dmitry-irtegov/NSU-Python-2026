#!/usr/bin/env python3

from sys import stderr


def input_safe(prompt):
    try:
        return input(prompt)
    except EOFError:
        print("\nException in input_safe(): EOF when reading a line", file=stderr)
        return None
    except KeyboardInterrupt:
        return None


def cumulative_sums(nums):
    res = [0]
    curr = 0
    for num in nums:
        curr += num
        res.append(curr)
    return res


if __name__ == "__main__":
    s = input_safe("Enter numbers separated by spaces: ")
    if s is not None:
        try:
            print(cumulative_sums([int(x) for x in s.split()]))
        except ValueError as err:
            print(f"Exception in main(): {err}", file=stderr)
