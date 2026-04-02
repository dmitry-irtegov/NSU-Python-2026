from sys import stderr

def get_stats(digits):
    res_cnt = 0
    res_list = []
    cur_str = ""
    start_pos_in_file = 0
    with open("pi.txt", "r") as file:
        for line in file:
            cur_str += line.rstrip("\n").split(".")[-1]
            if len(cur_str) < len(digits):
                continue
            start_pos = 0
            pos = cur_str.find(digits, start_pos)
            while pos != -1:
                res_cnt += 1
                if len(res_list) < 5:
                    res_list.append(pos+start_pos_in_file)
                start_pos = pos + 1
                pos = cur_str.find(digits, start_pos)
            start_pos_in_file += len(cur_str)-len(digits) + 1
            cur_str = cur_str[len(cur_str)-len(digits) + 1:]
    return res_cnt, res_list



if __name__ == '__main__':
    try:
        digits = input()
        if not(digits.isdigit()):
            raise Exception("Invalid input")
        res_cnt, res_list = get_stats(digits)
        print(f'Found count: {res_cnt}\nFound list: {res_list}')

    except Exception as ex:
        print("Exception raised", ex, file=stderr)
        exit(1)


