#!/usr/bin/python


def compute(inp: list) -> list:
    out = [0]
    for i in inp:
        out.append(out[-1] + i)
    return out


def test():
    from random import randint

    def test_case():
        arr = [randint(-100, 100) for _ in range(100)]
        new_arr = compute(arr)
        original_arr = []
        for i in range(len(new_arr)-1):
            original_arr.append(new_arr[i+1] - new_arr[i])
        assert  original_arr == arr

    for i in range(100):
        test_case()

if __name__ == "__main__":
    test()