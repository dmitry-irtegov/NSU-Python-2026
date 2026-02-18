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

print(to_prime(int(input())))