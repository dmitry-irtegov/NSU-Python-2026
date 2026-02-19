def number_to_words(n: int) -> str:
    words = ["no", "one", "two", "three", "four", "five",
             "six", "seven", "eight", "nine", "ten"]
    return words[n]

def ten_green_bottles():
    for n in range(10, 0, -1):
        bottle_word = "bottle" if n == 1 else "bottles"
        next_bottle_word = "bottle" if n-1 == 1 else "bottles"
        
        print(f"{number_to_words(n).capitalize()} green {bottle_word} hanging on the wall,")
        print(f"{number_to_words(n).capitalize()} green {bottle_word} hanging on the wall,")
        
        print(f"{'And if' if n > 1 else 'If that'} one green bottle should accidentally fall,")
        print(f"There’ll be {number_to_words(n-1)} green {next_bottle_word} hanging on the wall.")
        

mock_text = ""
def mock_print(*text):
    global mock_text
    mock_text += " ".join(map(str, text)) + "\n"

def test():
    global print
    old_print = print
    print = mock_print
    ten_green_bottles()
    print = old_print 

    expected_text = """Ten green bottles hanging on the wall,
Ten green bottles hanging on the wall,
And if one green bottle should accidentally fall,
There’ll be nine green bottles hanging on the wall.
Nine green bottles hanging on the wall,
Nine green bottles hanging on the wall,
And if one green bottle should accidentally fall,
There’ll be eight green bottles hanging on the wall.
Eight green bottles hanging on the wall,
Eight green bottles hanging on the wall,
And if one green bottle should accidentally fall,
There’ll be seven green bottles hanging on the wall.
Seven green bottles hanging on the wall,
Seven green bottles hanging on the wall,
And if one green bottle should accidentally fall,
There’ll be six green bottles hanging on the wall.
Six green bottles hanging on the wall,
Six green bottles hanging on the wall,
And if one green bottle should accidentally fall,
There’ll be five green bottles hanging on the wall.
Five green bottles hanging on the wall,
Five green bottles hanging on the wall,
And if one green bottle should accidentally fall,
There’ll be four green bottles hanging on the wall.
Four green bottles hanging on the wall,
Four green bottles hanging on the wall,
And if one green bottle should accidentally fall,
There’ll be three green bottles hanging on the wall.
Three green bottles hanging on the wall,
Three green bottles hanging on the wall,
And if one green bottle should accidentally fall,
There’ll be two green bottles hanging on the wall.
Two green bottles hanging on the wall,
Two green bottles hanging on the wall,
And if one green bottle should accidentally fall,
There’ll be one green bottle hanging on the wall.
One green bottle hanging on the wall,
One green bottle hanging on the wall,
If that one green bottle should accidentally fall,
There’ll be no green bottles hanging on the wall.""" + "\n"

    print(mock_text)
    assert mock_text == expected_text

if __name__ == "__main__":
    test()
