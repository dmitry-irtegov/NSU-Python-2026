from random import randint, choice, seed
from string import ascii_lowercase
from sys import stderr

def generate():
    latin_words = [
        "aqua", "terra", "ignis", "ventus", "sol", "luna", "stella",
        "arbor", "flos", "herba", "canis", "felis", "equus", "taurus",
        "homo", "vir", "mulier", "puer", "puella", "rex", "regina",
        "domus", "via", "pons", "porta", "fenestra", "mensa", "sella",
        "liber", "scriptum", "verbum", "nomen", "littera", "numerus",
        "tempus", "dies", "nox", "hora", "annus", "mensis", "septimana"
    ]

    seed(1)

    cnt = 0
    letters = ascii_lowercase
    my_words = set()
    while cnt < 10**5:
        length = randint(10, 20)
        word = ''.join(choice(letters) for _ in range(length))

        while word in my_words:
            word = ''.join(choice(letters) for _ in range(length))
        my_words.add(word)
        cnt += 1


    try:
        with open("hard.txt", "w", encoding="utf-8") as file:
            for word in my_words:
                cnt_to_transl = randint(1, 4)
                trans_list = [latin_words[randint(0, len(latin_words) - 1)] for _ in range(cnt_to_transl)]
                line = f'{word} - '
                for tr in trans_list:
                    line += f'{tr}, '
                line = line[:-2] + "\n"
                file.write(line)


    except FileNotFoundError:
        print("Wrong file path", file=stderr)
        exit(1)
    except PermissionError:
        print("No rights for file", file=stderr)
        exit(1)
    except IsADirectoryError:
        print("file is not a regular", file=stderr)
        exit(1)
    except OSError as e:
        print(f"os error: {e}", file=stderr)
        exit(1)
