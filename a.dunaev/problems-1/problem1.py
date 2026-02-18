def compute(inp: list) -> list:
    out = [0]
    for i in inp:
        out.append(out[-1] + i)
    return out