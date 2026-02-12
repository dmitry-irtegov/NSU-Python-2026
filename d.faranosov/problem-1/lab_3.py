from sys import argv, stderr

def hyp(num):
    nums = [num]
    while num != 1:
        if num % 2 == 0:
            num //= 2
            nums.append(num)
        else:
            num = num * 3 +1
            nums.append(num)

    for temp in nums[:-1]:
        print(f'{temp}->', end="")
    print(f'{nums[-1]}')

if len(argv) < 2:
    print("No num to check", file=stderr)
num = int(argv[1])
hyp(num)