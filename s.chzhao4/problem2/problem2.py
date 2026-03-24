def invert_dictionary(lines: list) -> list:
    latin_to_english = {}

    for line in lines:
        if '-' not in line:
            continue

        parts = line.split('-')
        eng_word = parts[0].strip()
        lat_translations_str = parts[1].strip()

        lat_words = [w.strip() for w in lat_translations_str.split(',')]

        for lat in lat_words:
            if lat not in latin_to_english:
                latin_to_english[lat] = []
            latin_to_english[lat].append(eng_word)

    result_lines = []
    sorted_latin_keys = sorted(latin_to_english.keys())

    for lat in sorted_latin_keys:
        eng_translations = sorted(latin_to_english[lat])
        result_lines.append(f"{lat} - {', '.join(eng_translations)}")

    return result_lines


def main():
    lines = [
        "apple - malum, pomum, popula",
        "fruit - baca, bacca, popum",
        "punishment - malum, multa"
    ]

    inverted_lines = invert_dictionary(lines)

    for line in inverted_lines:
        print(line)


if __name__ == "__main__":
    main()