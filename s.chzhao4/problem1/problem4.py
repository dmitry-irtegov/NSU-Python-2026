def sing_ten_green_bottles() -> None:
    numbers = [
        "No", "One", "Two", "Three", "Four",
        "Five", "Six", "Seven", "Eight", "Nine", "Ten"
    ]

    for i in range(10, 0, -1):
        current_num_word = numbers[i]
        next_num_word = numbers[i - 1].lower()

        # 处理单复数：1个瓶子用 bottle，其他用 bottles
        bottle_str = "bottle" if i == 1 else "bottles"

        # 下一个状态的单复数：如果是1减到0，0用bottles；如果是2减到1，1用bottle
        next_bottle_str = "bottle" if (i - 1) == 1 else "bottles"

        line = f"{current_num_word} green {bottle_str} hanging on the wall,"

        print(line)
        print(line)

        if i == 1:
            print("If that one green bottle should accidentally fall,")
        else:
            print("And if one green bottle should accidentally fall,")

        print(f"There'll be {next_num_word} green {next_bottle_str} hanging on the wall.")

if __name__ == "__main__":
    sing_ten_green_bottles()