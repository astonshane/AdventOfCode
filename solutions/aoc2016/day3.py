from register import register_solution
import re


@register_solution(2016, 3, 1)
def part1(filename):
    count = 0
    with open(filename) as f:
        for line in f:
            m = re.search('(\d+)\s+(\d+)\s+(\d+)', line.strip())
            nums = [int(m.groups()[i]) for i in range(0, 3)]
            nums.sort()
            if nums[0] + nums[1] > nums[2]:
                count += 1

    print(count)


@register_solution(2016, 3, 2)
def part2(filename):
    count = 0
    lines = []
    line_count = 0

    with open(filename) as f:
        for line in f:
            line_count += 1
            m = re.search('(\d+)\s+(\d+)\s+(\d+)', line.strip())
            nums = [int(m.groups()[i]) for i in range(0, 3)]
            lines.append(nums)

            if line_count == 3:
                for i in range(0, 3):
                    triangle = []
                    for j in range(0, 3):
                        triangle.append(lines[j][i])

                    triangle.sort()
                    if triangle[0] + triangle[1] > triangle[2]:
                        count += 1

                lines = []
                line_count = 0

    print(count)
