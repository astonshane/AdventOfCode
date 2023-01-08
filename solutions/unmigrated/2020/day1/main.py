import copy

all_nums = []
with open("input.txt") as f:
    for num in f:
        all_nums.append(int(num))

def recurse(max_size, all_nums, nums=[]):
    if len(nums) == max_size:
        if sum(nums) == 2020:
            prod = 1
            for x in nums:
                prod *= x
            print(nums, prod)
    else:
        for i in range(0, len(all_nums)):
            new_nums = copy.copy(nums)
            new_nums.append(all_nums[i])
            recurse(max_size, all_nums[i+1:], new_nums)

recurse(2, all_nums)
recurse(3, all_nums)