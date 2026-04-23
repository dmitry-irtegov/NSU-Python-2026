#!/usr/bin/env python3.12
from sys import stderr, exit


def cumulative_sums(numbers):
        
    result = [0]
    currentSum = 0
    for element in numbers:
        currentSum += element
        result.append(currentSum)
    return result
    

if __name__ == '__main__':
    while True:
        try:
            input_string = input('Введите числа: ')
            list = map(int, input_string.split())
            result = cumulative_sums(list)
            print('Результат:', result)
            break
        except ValueError as e:
            print(f'Входные данные не числа:\n {e}', file=stderr)
        except KeyboardInterrupt:
            print("KeyboardInterrupt received", file=stderr)
            exit()
        except EOFError:
            print("EOFError received", file=stderr)
            exit()
        except Exception as e:
            print(f"Ошибка:\n {e}", file=stderr)
            exit()

