#!/usr/bin/env python3.12

def tenGreenBottles():
    str_numbers = ['Ten', 'Nine', 'Eight', 'Seven', 'Six', 'Five', 'Four', 'Three', 'Two', 'One', 'No']

    first_line = ' green bottle{s} hanging on the wall,'
    third_line = '{} one green bottle should accidentally fall{}'
    fourth_line = ' green bottle{} hanging on the wall.'

    for i in range(10):
        print(str_numbers[i] + first_line.format(s = 's' if i != 9 else ''))
        print(str_numbers[i] + first_line.format(s = 's' if i != 9 else ''))
        print(third_line.format('And if' if i != 9 else 'If that', ',' if i != 9 else ''))
        print("There'll be " + str_numbers[i + 1].lower() + fourth_line.format('s' if i != 9 else '') + "\n")


if __name__ == '__main__':
    tenGreenBottles()
    