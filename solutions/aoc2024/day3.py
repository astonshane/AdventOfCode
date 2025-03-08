from register import register_solution
import re


@register_solution(2024, 3, 1)
def part1(filename):
    with open(filename) as f:
        total = 0
        p = re.compile('(mul\((\d+),(\d+)\))')
        for line in f:
            groups = p.findall(line)
            for group in groups:
                total += int(group[1]) * int(group[2])
        print(total)


def calculate(line):
    total = 0
    p = re.compile('(mul\((\d+),(\d+)\))')
    groups = p.findall(line)
    for group in groups:
        total += int(group[1]) * int(group[2])
    return total


@register_solution(2024, 3, 2)
def part2(filename):
    with open(filename) as f:
        total = 0
        line = ""
        for x in f:
            line += x

        p = re.compile('(do\(\)|don\'t\(\)|mul\((\d+),(\d+)\))')
        groups = p.findall(line)
        enabled = True
        for group in groups:
            if group[0] == "do()":
                enabled = True
            elif group[0] == "don't()":
                enabled = False
            else:
                if enabled:
                    total += int(group[1]) * int(group[2])
        print(total)
