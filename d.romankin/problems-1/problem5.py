import random

def factorize(n : int) -> list[list]:
    factors = []
    d = 2    
    while d * d <= n:
        if n % d == 0:
            count = 0
            while n % d == 0:
                count += 1
                n //= d
            factors.append([d, count])
        d += 1
    
    if n > 1:
        factors.append([n, 1])
        
    return factors


if __name__ == "__main__":
    random.seed()
    num = random.randint(1, 10000000000)
    print(num)
    res = factorize(num)
    prod = 1
    for i in res:       
        prod *= (i[0]**i[1])
    print(prod)
    assert(prod == num)