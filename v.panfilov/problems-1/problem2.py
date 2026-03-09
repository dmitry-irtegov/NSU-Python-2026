#!/usr/bin/env python3.12
import unittest
from sys import stderr, exit


def fltr(list, a: int, b: int):
    if b < a:
        raise ValueError("Верхний лимит должен быть больше нижнего")
    result = [max(min(elem, b), a) for elem in list]
    return result


class TestFltr(unittest.TestCase):
    def test_normal(self):
        self.assertEqual(fltr([1, 5, 10, -3, 7], 2 ,8), [2, 5, 8, 2, 7])
    
    def test_limit(self):
        self.assertRaises(ValueError, fltr, [1], 2, 1)

    def test_border_values(self):
        self.assertEqual(fltr([-5, 0, 5, 10], -5, 10), [-5, 0, 5, 10])

    def test_empty_array(self):
        self.assertEqual(fltr([], 0, 10), [])

    def test_negative_values(self):
        self.assertEqual(fltr([-10, -5, 0, 5, 10], -3, 3), [-3, -3, 0, 3, 3])
    
    def test_float_values(self):
        self.assertEqual(fltr([1.5, 2.7, 3.2, 4.8], 2.0, 4.0), [2.0, 2.7, 3.2, 4.0])

    def test_same_border(self):
        self.assertEqual(fltr([1, 2, 3, 4, 5, 6, 7], 3, 3), [3, 3, 3, 3, 3, 3, 3])

    

if __name__ == '__main__':
    while True:
        try:
            list = input('Enter the list: ')
            a = int(input('lower bound: '))
            b = int(input('upper bound: '))
            result = fltr(map(int, list.split()), a, b)
            print('Answer for the list is: ', result)
            break
        except ValueError as e:
            print(f'Неверные входные данные:\n{e}', file=stderr)
        except KeyboardInterrupt:
            print("KeyboardInterrupt received", file=stderr)
            exit()
        except EOFError:
            print("EOFError received", file=stderr)
            exit()
        except Exception as e:
            print(f"Ошибка:\n {e}", file=stderr)
            exit()
    print('Тесты:')
    unittest.main()