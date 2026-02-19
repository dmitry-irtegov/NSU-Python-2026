
def green_bottles():
    numbers = ["Ten", "Nine", "Eight", "Seven", "Six", "Five", "Four", "Three", "Two", "One", "no"]
    length = len(numbers)
    for i in range(length - 1):
        for j in range(2):
            print(numbers[i] + " " + "green bottle" + ("" if i == length - 2 else "s") + " hanging on the wall,")
        print(("And if " if i != length - 2 else "If that ") + "one green bottle should accidentally fall,")
        print("There’ll be " + numbers[i + 1].lower() + " green bottles hanging on the wall.")


mock_text = ""
def mock_print(*args):
    global mock_text
    for i in args:
        mock_text += str(i) + '\n'

def test():
    global print
    old_print = print
    print = mock_print
    green_bottles()
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
There’ll be one green bottles hanging on the wall.
One green bottle hanging on the wall,
One green bottle hanging on the wall,
If that one green bottle should accidentally fall,
There’ll be no green bottles hanging on the wall.""" + "\n"

    print(mock_text)
    assert mock_text == expected_text

if __name__ == "__main__":
    test()