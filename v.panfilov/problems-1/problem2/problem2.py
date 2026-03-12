#!/usr/bin/env python3.12
from sys import stderr, exit


def fltr(list, a: int, b: int):
    if b < a:
        raise ValueError("Верхний лимит должен быть больше нижнего")
    result = [max(min(elem, b), a) for elem in list]
    return result
    

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