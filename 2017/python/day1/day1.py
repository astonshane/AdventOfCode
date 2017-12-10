import sys

def part1():
    filename = sys.argv[1]
    with open(filename) as input:
        nums = input.readline().strip()
        nums += nums[0]

        total = 0
        for i in range(0, len(nums)-1):
            a = nums[i]
            b = nums[i+1]
            if a == b:
                total += int(a)
        print "Part1():", total

def part2():
    filename = sys.argv[1]
    with open(filename) as input:
        nums = input.readline().strip()
        rotate = len(nums) / 2

        total = 0
        for i in range(0, len(nums)):
            a = nums[i]
            b = nums[(i+rotate) % len(nums)]
            if a == b:
                total += int(a)
        print "Part2():", total

part1()
part2()
