def limit(inp: list, a: int, b: int) -> list:
    return list(map(lambda x: a if x < a else (b if x > b else x), inp))

if __name__ == "__main__":
    inp = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    a, b = 3, 7
    assert limit(inp, a, b) == [3, 3, 3, 4, 5, 6, 7, 7, 7]

    inp = [6, 5, 2, 7, -1, 5, 2, 10]
    a, b = 3, 9
    assert limit(inp, a, b) == [6, 5, 3, 7, 3, 5, 3, 9]