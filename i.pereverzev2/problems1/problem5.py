#!/usr/bin/python


def toprimes(num):
    divider = 2
    prime_list = []
    curr_power = 0
    while num != 1:
        if num % divider == 0:
            num //= divider
            curr_power += 1
        else:
            if curr_power != 0:
                prime_list.append([divider, curr_power])
            divider += 1
            curr_power = 0
    prime_list.append([divider, curr_power])
    return prime_list


if __name__ == "__main__":
    print(toprimes(int(input())))
