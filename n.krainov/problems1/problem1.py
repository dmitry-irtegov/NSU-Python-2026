def cumulative_sum(numList):
    if len(numList) == 0:
        return [0]

    res = [0]
    for i in range(len(numList)):
        res.append(res[-1] + numList[i])

    return res

assert cumulative_sum([10, 20, 30]) == [0, 10, 30, 60]
assert cumulative_sum([0]) == [0, 0]
assert cumulative_sum([]) == [0]

if __name__ == '__main__':
    listLen = input("Please enter a list length: ")
    listNums = []

    if not listLen.isdigit():
        print("It's not a number")
        exit(1)

    listLen = int(listLen)

    if listLen < 0:
        print("List can't have negative length")
        exit(1)

    if listLen != 0:
        print("Please enter list numbers")

    for i in range(listLen):
        num = input()
        if not num.isdigit():
            print("It's not a number")
            exit(1)

        listNums.append(int(num))

    print(cumulative_sum(listNums))
