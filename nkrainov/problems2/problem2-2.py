
def build_dictionary(input_dict):
    latin_to_english = dict()
    for line in input_dict:
        cleaned = line.replace(',', ' ').replace('-', ' ')
        words = cleaned.split()
        if len(words) < 2:
            raise ValueError("incorrect format of line")

        for word in words[1:]:
            if word not in latin_to_english:
                latin_to_english[word] = list()

            latin_to_english[word].append(words[0])

    ret = []
    for key in sorted(latin_to_english.keys()):
        ret.append(key + "-" + ', '.join(latin_to_english[key]))

    return ret


if __name__ == "__main__":
    path = input("please enter the file path: ")
    try:
        lines = open(path, "r").readlines()
    except Exception as e:
        print("error occurred during opening file", e)
        exit(1)

    try:
        latin_to_english = build_dictionary(lines)
    except ValueError as e:
        print("error occurred during building dictionary", e)
        exit(1)

    print(latin_to_english)


