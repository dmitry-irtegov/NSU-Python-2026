from sys import argv, stderr
from math import gcd


def get_triples(max_num):
    triples = []
    m = 1
    while m*m+1 < max_num:
        n = m % 2 + 1
        while n < m:
            if m*m+n*n < max_num and check_simple(n, m):
                triples.append(get_triple(m, n))
                koef = 2
                while koef*(m*m+n*n) < max_num:
                    pretendent = get_triple(m, n, koef)
                    triples.append(pretendent)
                    koef += 1
            n += 2
        m += 1
    return sorted(triples, key=lambda x: x[2])


def get_triple(m,n, koef=1):
    return (koef*(m*m-n*n), koef*2*m*n, koef*(m*m+n*n))


def check_simple(num1, num2):
    nod = gcd(num1, num2)
    return nod == 1


if __name__ == '__main__':
    try:
        max_num = int(argv[1])
        triples = get_triples(max_num)
        print(triples)
    except ValueError:
        print("Wrong max number", file=stderr)
        exit(1)
