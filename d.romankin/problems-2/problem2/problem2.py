from sys import argv, stderr



def main(filename):
    """function that makes language2-language1 dictionary from language1-lamguage2 dictionary
    filename - path to file with dictionary
    dictionary format example:
    apple - malum, pomum, popula
    fruit - baca, bacca, popum
    punishment - malum, multa
    """
    

    try:
        file = open(filename, 'r')
    except OSError as err:
        print("Cannot open the file", err, file=stderr)
        return


    dictionary : dict[str, list[str]] = {}
    lines = file.readlines()
    
    for line in lines:
        spl = line.split(" - ")
        str_arr = [word.strip() for word in spl[1].split(",")]
        dictionary[spl[0]] = str_arr
        
    res_dictionary : dict[str, list[str]] = {}

    for k,v in dictionary.items():
        for word in v:
            words = res_dictionary.get(word, [])
            words.append(k)
            res_dictionary[word] = words

    for words in res_dictionary.values():
        words.sort()

    sorted_res_dictionary = sorted(res_dictionary)
    for word in sorted_res_dictionary:
        print(word, "-", end=" "),
        word_list = res_dictionary[word]
        length = len(word_list)
        for i in range(length):
            print(word_list[i], end=", " if i != (length - 1) else "")
        print("", end = "\n" if (sorted_res_dictionary.index(word) != len(sorted_res_dictionary) - 1) else "")
    file.close()

if __name__ == "__main__":
    if (len(argv) != 2):
        print("usage: python problem2.py <file_name>")
    else:
        main(argv[1])
        print("")