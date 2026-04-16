from collections import defaultdict

def parse_entries(text):
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    if not lines:
        return []

    if lines[0].isdigit():
        count = int(lines[0])
        return lines[1 : count + 1]

    return lines


def invert_dictionary(entries):
    latin_to_english = defaultdict(list)

    for entry in entries:
        english_word, latin_words = entry.split(" - ")
        for latin_word in latin_words.split(", "):
            latin_to_english[latin_word].append(english_word)

    return {
        latin_word: sorted(english_words)
        for latin_word, english_words in sorted(latin_to_english.items())
    }


def format_dictionary(latin_to_english):
    return "\n".join(
        f"{latin_word} - {', '.join(english_words)}"
        for latin_word, english_words in latin_to_english.items()
    )


def solve(text):
    return format_dictionary(invert_dictionary(parse_entries(text)))


def main():
    with open("data.txt", encoding="utf-8") as file:
        print(solve(file.read()), end="")


if __name__ == "__main__":
    main()
