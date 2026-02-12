def factorize(n : int) -> list[list]:
    factors = []
    d = 2
    temp = n
    
    while d * d <= temp:
        if temp % d == 0:
            count = 0
            while temp % d == 0:
                count += 1
                temp //= d
            factors.append([d, count])
        d += 1
    
    if temp > 1:
        factors.append([temp, 1])
        
    return factors