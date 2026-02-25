import argparse


def build_latin_to_english_dict(lines: list[str]) -> dict[str, list[str]]:
    latin_to_english: dict[str, list[str]] = {}

    for line in lines:
        line = line.strip()
        if not line:
            continue

        english, latin_words = line.split(" - ")
        for latin in latin_words.split(", "):
            latin_to_english.setdefault(latin, []).append(english)

    return {
        latin: sorted(english_list)
        for latin, english_list in sorted(latin_to_english.items())
    }


def build_from_file(input_filename: str, output_filename: str):
    with open(input_filename, "r", encoding="utf-8") as infile:
        lines = infile.readlines()

    result_dict = build_latin_to_english_dict(lines)

    with open(output_filename, "w", encoding="utf-8") as outfile:
        for latin, english_words in result_dict.items():
            outfile.write(f"{latin} - {', '.join(english_words)}\n")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("input_file", help="Path to input file")
    parser.add_argument("output_file", help="Path to output file")

    args = parser.parse_args()

    build_from_file(args.input_file, args.output_file)