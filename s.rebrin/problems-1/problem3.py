#!/usr/bin/python

def collatz(num: int) -> list[int]:
    if num <= 0:
        raise ValueError("Number must be positive")
    res: list[int] = []
    while num != 1:
        res.append(num)
        if num % 2 == 0:
            num = num // 2
        else:
            num = num * 3 + 1
    res.append(num)
    return res


def run_test():
    assert collatz(6) == [6, 3, 10, 5, 16, 8, 4, 2, 1]

    assert collatz(1) == [1]

    assert collatz(3) == [3, 10, 5, 16, 8, 4, 2, 1]

    try:
        collatz(0)
        assert False
    except ValueError:
        pass

    try:
        collatz(-5)
        assert False
    except ValueError:
        pass

    print("ALL TESTS PASSED")


def main() -> None:
    while True:
        try:
            a = int(input())
            break
        except ValueError:
            print("Need number")
            continue
        break
    res = collatz(a)
    print(" -> ".join(map(str, res)))


from sys import argv

if __name__ == "__main__":
    if "test" in argv:
        run_test()
    else:
        main()
