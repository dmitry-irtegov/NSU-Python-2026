#!/usr/bin/env python3.12
import unittest
import sys
from typing import List


def cumulative_sums(numbers):
        
    result = [0]
    currentSum = 0
    for element in numbers:
        currentSum += element
        result.append(currentSum)
    return result
    
class TestSums(unittest.TestCase):
    def test_1(self):
        self.assertEqual(cumulative_sums([1, 2, 3]), [0, 1, 3, 6])


    def test_2(self):
        self.assertEqual(cumulative_sums([0]), [0, 0])

    def test_3(self):
        self.assertEqual(cumulative_sums([]), [0])

    def test_4(self):
        self.assertEqual(cumulative_sums(range(1, 18)), [0, 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 105, 120, 136, 153])

    def test_5(self):
        self.assertEqual(cumulative_sums([1.5, 2.5, 3.5]), [0, 1.5, 4.0, 7.5])

if __name__ == '__main__':
    while True:
        try:
            input_string = input('Введите числа: ')
            list = map(int, input_string.split())
            result = cumulative_sums(list)
            print('Результат:', result)
            break
        except ValueError as e:
            print(f'Входные данные не числа:\n {e}')
    print('Тесты:', unittest.main())

