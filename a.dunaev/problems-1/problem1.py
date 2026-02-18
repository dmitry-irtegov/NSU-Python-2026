def compute(inp: list) -> list:
    out = [0]
    for i in inp:
        out.append(out[-1] + i)
    return out

if __name__ == "__main__":
    inp = [1, 2, 3]
    assert compute(inp) == [0, 1, 3, 6]

    inp = []
    assert compute(inp) == [0]

    inp = [4, 6, 4, 3, 2]
    assert compute(inp) == [0, 4, 10, 14, 17, 19]
