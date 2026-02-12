
from sys import stderr

def main(seq):
    """ function that gets indexes of subsequences in pi number
    seq - string subsequence
    """


    try:
        file = open('pi.txt', 'r')
    except OSError as err:
        print("Cannot open file ", err, file=stderr)
        return
    else:
        with file:
            data = file.read()
            data = ''.join(filter(str.isdigit, data[2:]))
            start = 0
            indexes = []
            while 1:
                cur_index = data.find(seq, start)
                if cur_index == -1:
                    break
                indexes.append(cur_index)
                start = cur_index + 1
                
            length = len(indexes)
            print("Found", (length), "results.")
            if (length > 0):
                print("Positions: ", end="")
                for i in indexes[0:5]:
                    print(i, end=" " if indexes.index(i) < min(5, length) - 1 else "")
                if length > 5:
                    print(" ...", end="")
                print("")

if __name__ == "__main__":
    seq = (input("Enter sequence to search for\n"))

    main(seq)