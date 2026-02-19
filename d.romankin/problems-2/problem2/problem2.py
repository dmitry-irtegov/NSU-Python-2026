from sys import argv, stderr

filename = argv[1]

try:
    file = open(filename, 'r')
except OSError:
    print("No such file!", file=stderr)


dictionary : dict[str, list[str]] = {}
line = file.readline()
while line:
    spl = line.split(" - ")
    str_arr = spl[1][:-1].split(", ")

    dictionary[spl[0]] = str_arr
    line = file.readline()

res_dictionary : dict[str, list[str]] = {}

for k,v in dictionary.items():
    for word in v:
        words = res_dictionary.get(word, [])
        words.append(k)
        res_dictionary[word] = words

for words in res_dictionary.values():
    words.sort()

for word in sorted(res_dictionary):
    print(word, " - ", res_dictionary[word])