def collatz_seq(number, maxIter = 1 << 61):
    seq = [number]
    n = number
    i = 0
    while n != 1:
        if i == maxIter:
            return False, []

        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1

        i += 1
        seq.append(n)

    return True, seq


assert collatz_seq(3) == (True, [3, 10, 5, 16, 8, 4, 2, 1])
