#!/usr/bin/python
def limit(inp, a, b):
    return list(map(lambda x: a if x < a else (b if x > b else x), inp))

if __name__ == '__main__':
    print(limit([1, 2, 3, 4, 5], 2, 4))