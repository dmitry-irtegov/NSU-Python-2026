#!/usr/bin/env python3

from sys import stderr


def input_safe(prompt):
    try:
        return input(prompt)
    except KeyboardInterrupt:
        return None
    except Exception as e:
        print(f"\nException in input_safe(): {e}", file=stderr)
        return None


def clip_nums(nums, a, b):
    res = []
    for num in nums:
        if num < a:
            res.append(a)
        elif num > b:
            res.append(b)
        else:
            res.append(num)
    return res


if __name__ == "__main__":
    bs = input_safe("Enter a and b separated by spaces: ")
    s = input_safe("Enter numbers separated by spaces: ")

    if bs is not None and s is not None:
        try:
            lb, ub = [float(x) for x in bs.split()]
            print(clip_nums([float(x) for x in s.split()], lb, ub))
        except Exception as err:
            print(f"Exception in main(): {err}", file=stderr)
