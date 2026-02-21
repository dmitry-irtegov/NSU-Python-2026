#!/usr/bin/python


def collatc(num):
    print(num, end="")
    while num != 1:
        if num % 2 == 0:
            num //= 2
        else:
            num = num * 3 + 1
        print(" -> ", num, end="")


if __name__ == "__main__":
    collatc(int(input()))
