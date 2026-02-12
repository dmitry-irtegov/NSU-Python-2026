from itertools import accumulate

def cumulative_sum(arr):
    return [0] + list(accumulate(arr))

def test():
    from random import randint
    def test_case():
        arr = [randint(-100, 100) for _ in range(randint(0, 100))]
        result = cumulative_sum(arr)

        original_arr = []
        for i in range(1, len(result)):
            original_arr.append(result[i] - result[i - 1])

        assert original_arr == arr

    for _ in range(100):
        test_case()

    print("ALL TESTS PASSED")

if __name__ == "__main__":
    test()
