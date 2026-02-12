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