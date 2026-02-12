def collatz_seq(number, maxIter = 1 << 61):
    def inner_func(n, iteration, num_seq):
        if iteration == maxIter:
            return False

        num_seq.append(n)
        if n == 1:
            return True

        if n % 2 == 0:
            return inner_func(n // 2, iteration + 1, num_seq)
        else:
            return inner_func(3 * n + 1, iteration + 1, num_seq)

    seq = []
    res = inner_func(number, 0, seq)

    return (res, seq) if res else (res, [])


assert collatz_seq(3) == (True, [3, 10, 5, 16, 8, 4, 2, 1])
