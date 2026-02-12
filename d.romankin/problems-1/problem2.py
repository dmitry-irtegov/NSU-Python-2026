import random

def cut(a, b, elems :list) -> list:
    if (a > b) :
        return []
    return [ a if i < a else b if i > b else i for i in elems ]

if __name__ == "__main__":
    random.seed()
    n = random.randint(1, 10**6)
    b = random.randint(-1 * (10**6), 10**6)
    a = random.randint(-1 * (10**6), b)
    arr = []
    for i in range(n):
        arr.append(random.randint(-1 * (10**6), 10**6))
    
    res = cut(a, b, arr)
    for i in res:
        assert(a <= i <= b)