#!/usr/bin/env python3.12
import unittest

def prime_factors(n: int) -> list[list[int]]:
    """
    Разлагает число n на простые множители и возвращает список пар [множитель, степень].

    Аргументы:
        n: целое число (n > 1 для содержательного разложения)

    Возвращает:
        Список вида [[p1, k1], [p2, k2], ...], где p_i — простые множители,
        k_i — их степени.
    """
    if not isinstance(n, int):
        raise ValueError("Number must be an Int.")

    if n < 1:
        raise ValueError("Number must be > zero.")

    if n == 1:
        return [[1, 1]]
    result = []
    multiplier = 2
    while multiplier * multiplier <= n:
        pow = 0
        while n % multiplier == 0:
            pow += 1
            n //= multiplier
        if pow > 0:
            result.append([multiplier, pow])
        else:
            multiplier += 1
    if n >= 1:
        result.append([n, 1])
    return result

class TestFactor(unittest.TestCase):
    def test_0(self):
        self.assertRaises(ValueError, prime_factors, 0)

    def test_1(self):
        self.assertEqual(prime_factors(1), [[1, 1]])

    def test_2(self):
        self.assertEqual(prime_factors(1000000000000), [[2, 12], [5, 12], [1, 1]])

    def test_3(self):
        self.assertRaises(ValueError, prime_factors, -1000000000000)

    def test_4(self):
        self.assertRaises(ValueError, prime_factors, 'text')


if __name__ == '__main__':
    try:
        a = int(input('Enter number: '))
        result = prime_factors(a)
        print(result)
        
    except ValueError:
        print("\nValue error received")
   

    print('Tests:', unittest.main())
