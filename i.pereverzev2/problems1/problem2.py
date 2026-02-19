#!/usr/bin/python


def clip(seq, a, b):
    res = []
    for num in seq:
        num = max(a, num)
        num = min(b, num)
        res.append(num)
    return res


if __name__ == "__main__":
    print(clip(map(float, input().split()), 1, 4))
