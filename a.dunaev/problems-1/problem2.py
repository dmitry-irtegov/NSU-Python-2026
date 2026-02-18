#!/usr/bin/python
def limit(inp: list, a: int, b: int) -> list:
    return list(map(lambda x: a if x < a else (b if x > b else x), inp))

def test():
    from random import randint

    def test_case():
        arr = [randint(-100, 100) for i in range(100)]
        ab = sorted([randint(-100, 100), randint(-100, 100)])

        new_arr = sorted(limit(arr, ab[0], ab[1]))

        assert (new_arr[0] >= ab[0]) and (new_arr[-1] <= ab[1])

    for i in range(100):
        test_case()

if __name__ == "__main__":
    test()