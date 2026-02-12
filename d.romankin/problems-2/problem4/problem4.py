file = open('pi.txt', 'r')
data = file.read()
seq = str(input("Enter sequence to search for\n"))
cur_index = 0

indexes = []
while 1:
    cur_index = data.find(seq, cur_index)
    if cur_index == -1:
        break
    else:
        indexes.append(cur_index)
        cur_index += len(seq)
        
length = len(indexes)
print("Found ", (length), " results")
print("Positions: ", str(indexes[0:5]), " . . ." if length > 5 else "")
file.close()