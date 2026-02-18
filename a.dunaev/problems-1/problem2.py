def limit(inp: list, a: int, b: int) -> list:
    return list(map(lambda x: a if x < a else (b if x > b else x), inp))