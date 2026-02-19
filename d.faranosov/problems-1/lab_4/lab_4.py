def write_poem():
    num_dict = {0: "No", 1: "One", 2: "Two", 3:"Three", 4:"Four", 5:"Five",
            6:"Six", 7:"Seven", 8:"Eight", 9:"Nine", 10:"Ten"}
    for i in range(10, 0, -1):
        for j in range(2):
            print(f"{num_dict[i]} green bottle{'' if i == 1 else 's'} hanging on the wall,")
        print("And if one green bottle should accidentally fall,")
        print(f"There`ll be {num_dict[i-1].lower()} green bottles hanging on the wall.")


if __name__ == '__main__':
    write_poem()