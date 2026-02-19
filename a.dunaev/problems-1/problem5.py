#!/usr/bin/python

def to_prime(n: int) -> list:
    if n == 0: return []
    out = []
    num = n
    prime = [True] * (num + 1)
    prime[0] = False
    prime[1] = False

    for i in range(2, int(num) + 1, 1):
        if prime[i]:

            tmp = [i, 0]

            while n % i == 0:
                n //= i
                tmp[1] += 1

            if tmp[1]:
                out.append(tmp)

            for j in range(i*i, num + 1, i):
                prime[j] = False

    return out

if __name__ == "__main__":
    num = 12
    assert to_prime(num) == [[2, 2], [3, 1]]

    num = 60
    assert to_prime(num) == [[2, 2], [3, 1], [5, 1]]