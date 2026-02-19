from random import randint
import unittest


def acc_sums(numbers):
    new_value = 0

    for i in range(len(numbers)):
       tmp = numbers[i]
       numbers[i] = new_value
       new_value += tmp
    numbers.append(new_value)

    return numbers


class TestAccSums(unittest.TestCase):

    def test_growing(self):
        size = randint(1, 1000)
        arr = [randint(-1000, 1000) for i in range(size)]
        self.assertTrue(len(arr) < len(acc_sums(arr)))


unittest.main()