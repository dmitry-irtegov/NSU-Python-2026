#!/usr/bin/python


def cumulative_sums(seq):
    result = [0]
    current = 0
    for num in seq:
        current += num
        result.append(current)
    return result


if __name__ == "__main__":
    print(cumulative_sums(map(float, input().split())))
