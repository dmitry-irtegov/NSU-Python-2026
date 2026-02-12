from sys import argv

def summarise(nums: []):
    res = [0]
    cur_sum = 0
    for num in nums:
        cur_sum += num
        res.append(cur_sum)
    return res

nums = [float(num) for num in argv[1:]]
print(summarise(nums))