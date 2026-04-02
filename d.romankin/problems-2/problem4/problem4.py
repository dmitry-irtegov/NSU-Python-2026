from cProfile import run as profile, runctx

from sys import stderr, argv
from enum import Enum
from re import sub
class Replacement(Enum):
    REPLACE = 1,
    FILTER = 2,
    REGEXP = 3,
    LIST = 4 


def main(seq, replace=Replacement.REPLACE):
    """ function that gets indexes of subsequences in pi number
    seq - string subsequence
    """


    try:
        with open("pi.txt", "r") as file:
            file.read(2)
            data = file.read()
            
            if replace == Replacement.FILTER:
                data = ''.join(filter(str.isdigit, data))
            elif replace == Replacement.REGEXP:
                data = sub(r"\D", "", data)
            elif replace == Replacement.LIST:
                data = ''.join([x for x in data if x.isdigit()])
            elif replace == Replacement.REPLACE:
                data = data.replace("\n", "")        
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
    except OSError as err:
        print("Cannot open file ", err, file=stderr)
        return        

def compare_replaces(replace):
    try:
        with open("pi.txt", "r") as file:
                file.read(2)
                data = file.read()
                
                if replace == Replacement.FILTER:
                    runctx("data = ''.join(filter(str.isdigit, data))", globals(), {'data' : data})
                elif replace == Replacement.REGEXP:
                    runctx(r"data = sub(r'\D', '', data)", globals(), {'data' : data})
                elif replace == Replacement.LIST:
                    runctx("data = ''.join([x for x in data if x.isdigit()])", globals(), {'data' : data})
                elif replace == Replacement.REPLACE:
                    runctx(r"data = data.replace('\n', '')", globals(), {'data' : data})        
            
    except OSError as err:
        print("Cannot open file ", err, file=stderr)
        return      
if __name__ == "__main__":
    try:
        
        if (len(argv) >= 2):
            if argv[1] == "profile":
                for rep in Replacement:
                    print("\n\n---PROFILING %s ---\n\n" % rep.name)
                    compare_replaces(rep)    

            else:
                seq = (input("Enter sequence to search for\n"))
                main(seq)
        else:
            seq = (input("Enter sequence to search for\n"))
            main(seq)
    except EOFError as eof:
        print("EOF error occured", eof, file=stderr)
    except Exception as e:
        print("Exception occured", e, file=stderr)


    