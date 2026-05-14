import unittest


def sing_the_song() -> list[str]:
    numbers: list[str] = [
        "no",
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine",
        "ten",
    ]

    song_lines: list[str] = []

    bottles_number: int = 10
    while bottles_number > 0:
        first_line: str = (
            f"{numbers[bottles_number].capitalize()} green bottle{'s' if bottles_number > 1 else ''} hanging on the wall,"
        )
        song_lines.append(first_line)
        song_lines.append(first_line)

        third_line: str = (
            f"{'And if' if bottles_number > 1 else 'If that'} one green bottle should accidentally fall,"
        )
        song_lines.append(third_line)

        bottles_number -= 1

        fourth_line: str = (
            f"There'll be {numbers[bottles_number]} green bottle{'s' if bottles_number != 1 else ''} hanging on the wall."
        )
        song_lines.append(fourth_line)
    return song_lines


class TestSingTheSong(unittest.TestCase):
    def test_song_equals_expected_text(self) -> None:
        expected: str = (
            "Ten green bottles hanging on the wall,\n"
            "Ten green bottles hanging on the wall,\n"
            "And if one green bottle should accidentally fall,\n"
            "There'll be nine green bottles hanging on the wall.\n"
            "Nine green bottles hanging on the wall,\n"
            "Nine green bottles hanging on the wall,\n"
            "And if one green bottle should accidentally fall,\n"
            "There'll be eight green bottles hanging on the wall.\n"
            "Eight green bottles hanging on the wall,\n"
            "Eight green bottles hanging on the wall,\n"
            "And if one green bottle should accidentally fall,\n"
            "There'll be seven green bottles hanging on the wall.\n"
            "Seven green bottles hanging on the wall,\n"
            "Seven green bottles hanging on the wall,\n"
            "And if one green bottle should accidentally fall,\n"
            "There'll be six green bottles hanging on the wall.\n"
            "Six green bottles hanging on the wall,\n"
            "Six green bottles hanging on the wall,\n"
            "And if one green bottle should accidentally fall,\n"
            "There'll be five green bottles hanging on the wall.\n"
            "Five green bottles hanging on the wall,\n"
            "Five green bottles hanging on the wall,\n"
            "And if one green bottle should accidentally fall,\n"
            "There'll be four green bottles hanging on the wall.\n"
            "Four green bottles hanging on the wall,\n"
            "Four green bottles hanging on the wall,\n"
            "And if one green bottle should accidentally fall,\n"
            "There'll be three green bottles hanging on the wall.\n"
            "Three green bottles hanging on the wall,\n"
            "Three green bottles hanging on the wall,\n"
            "And if one green bottle should accidentally fall,\n"
            "There'll be two green bottles hanging on the wall.\n"
            "Two green bottles hanging on the wall,\n"
            "Two green bottles hanging on the wall,\n"
            "And if one green bottle should accidentally fall,\n"
            "There'll be one green bottle hanging on the wall.\n"
            "One green bottle hanging on the wall,\n"
            "One green bottle hanging on the wall,\n"
            "If that one green bottle should accidentally fall,\n"
            "There'll be no green bottles hanging on the wall."
        )

        result: str = "\n".join(sing_the_song())
        self.assertEqual(result, expected)


if __name__ == "__main__":
    song: list[str] = sing_the_song()
    line: str
    for line in song:
        print(line)
