#!/usr/bin/python3

def narrow_list(arr, lower_bound, upper_bound):
    result = []
    for x in arr:
        if x > upper_bound:
            result.append(upper_bound)
        elif x < lower_bound:
            result.append(lower_bound)
        else:
            result.append(x)
    return result


def test():
    from random import randint

    def test_case():
        RANDOM_MAX = 10000
        RANDOM_MIN = -10000

        original_list = [randint(RANDOM_MIN, RANDOM_MAX) for i in range(1000)]
        lower_bound = randint(RANDOM_MIN, RANDOM_MAX)
        upper_bound = randint(lower_bound, RANDOM_MAX)
        new_list = narrow_list(original_list, lower_bound, upper_bound)
        assert (all([x <= upper_bound and x >= lower_bound for x in new_list])
                and len(new_list) == len(original_list))

    for _ in range(10000):
        test_case()


if __name__ == "__main__":
    test()
