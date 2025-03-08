from register import register_solution


def isSafe(line):
    increasing = True if line[1] > line[0] else False
    safe = True
    for i in range(0, len(line) - 1):
        if increasing and line[i+1] <= line[i]:
            safe = False
            break
        if not increasing and line[i+1] >= line[i]:
            safe = False
            break
        if abs(line[i] - line[i+1]) not in range(0, 4):
            safe = False
            break
    return safe

@register_solution(2024, 2, 1)
def part1(filename):
    with open(filename) as f:
        safe_count = 0
        for line in f:
            line = [int(x) for x in line.split()]
            if isSafe(line):
                safe_count += 1 
        print(safe_count)


@register_solution(2024, 2, 2)
def part2(filename):
    with open(filename) as f:
        safe_count = 0
        for line in f:
            line = [int(x) for x in line.split()]
            if isSafe(line):
                safe_count += 1
            else:
                for i in range(0, len(line)):
                    new_line = line[0:i] + line[i+1:]
                    if isSafe(new_line):
                        safe_count += 1
                        break
        print(safe_count)
