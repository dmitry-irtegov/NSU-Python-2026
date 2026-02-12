
def collatz(num: int):
    
    while (num != 1):
        print(num, end="->")
        num = num//2 if not (num%2) else 3 * num + 1
        
    print(num)



mock_text = ""
def mock_print(*args, end='\n'):
    global mock_text
    for i in args:
        mock_text += str(i) + end


def test():
    global print
    old_print = print
    print = mock_print
    collatz(3)
    collatz(7)
    print = old_print 
    print(mock_text)
    expected_text = "3->10->5->16->8->4->2->1" + '\n'
    expected_text += "7->22->11->34->17->52->26->13->40->20->10->5->16->8->4->2->1" + '\n'
    assert (mock_text == expected_text)
if __name__ == "__main__":
    num = int(input())
    if num > 0:
        collatz(num)
        test()
    else:
        print("Enter a positive number")
