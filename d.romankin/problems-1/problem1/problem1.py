import random
from numpy import array, append, cumsum
def cum(elems : list) -> list:
    sum = 0
    res = [0]
    for i in elems:
        sum += i
        res.append(sum)
    return res

if __name__ == "__main__":
    random.seed()
    n = random.randint(1, 10**6)
    
    ref_list = []
    
    
    for i in range(n):
        ref_list.append(random.randint(-1 * (10**6), 10**6))
    n_arr = array([0])
    n_arr = append(n_arr, (cumsum(ref_list)))
    assert(cum(ref_list) == list(n_arr))
