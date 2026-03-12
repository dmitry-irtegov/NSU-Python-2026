def apply_boundaries(numList, a, b):
    if a > b:
        raise ValueError("a can't be greater than b")

    res = map(lambda x: a if x < a else b if x > b else x, numList)

    return list(res)

if __name__ == '__main__':
    import sys

    try:
        a = input("Enter lower bound: ")
        a = int(a)

        b = input("Enter upper bound: ")
        b = int(b)

        listLen = input("Please enter a list length: ")
        listNums = []

        listLen = int(listLen)

        if listLen < 0:
            sys.stderr.write("List can't have negative length")
            exit(1)

        if listLen != 0:
            print("Please enter list numbers")

        for i in range(listLen):
            num = input()

            listNums.append(int(num))

        print(apply_boundaries(listNums, a, b))
    except Exception as e:
        sys.stderr.write("Error occurred: " + str(e))
        exit(1)