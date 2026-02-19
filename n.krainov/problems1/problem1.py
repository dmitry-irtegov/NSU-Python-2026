def cumulative_sum(numList):
    if len(numList) == 0:
        return [0]

    res = [0]
    for i in range(len(numList)):
        res.append(res[-1] + numList[i])

    return res

if __name__ == '__main__':
    try:
        listLen = input("Please enter a list length: ")
        listNums = []

        listLen = int(listLen)

        if listLen < 0:
            print("List can't have negative length")
            exit(1)

        if listLen != 0:
            print("Please enter list numbers")

        for i in range(listLen):
            num = input()
            listNums.append(int(num))

        print(cumulative_sum(listNums))
    except ValueError as e:
        print("error occurred: " + str(e))
        exit(1)
