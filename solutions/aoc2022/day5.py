import re
from register import register_solution


def parse_stacks(f):
    lines = []
    stacks = []
    while True:
        line = f.readline()
        if '1' in line:
            lines.reverse()
            i = 1
            while str(i) in line:
                stacks.append([])
                idx = line.index(str(i))
                for x in lines:
                    if x[idx] != ' ':
                        stacks[i-1].append(x[idx])
                i += 1
            break
        lines.append(line)
    f.readline()
    return stacks


@register_solution(2022, 5, 1)
def part1(filename):
    with open(filename) as f:
        stacks = parse_stacks(f)

        # continue reading the instructions
        r = re.compile(r'move (\d+) from (\d+) to (\d+)')
        for line in f:
            line = line.strip()
            m = r.match(line)
            count = int(m.group(1))
            frm = int(m.group(2))
            to = int(m.group(3))
            for _ in range(0, count):
                stacks[to-1].append(stacks[frm-1].pop())

        answer = ""
        for s in stacks:
            answer += s.pop()
        print("Part1:", answer)


@register_solution(2022, 5, 2)
def part2(filename):
    with open(filename) as f:
        stacks = parse_stacks(f)
    
        r = re.compile(r'move (\d+) from (\d+) to (\d+)')
        for line in f:
            line = line.strip()
            m = r.match(line)
            count = int(m.group(1))
            frm = int(m.group(2))
            to = int(m.group(3))

            to_move = stacks[frm-1][-count:]
            stacks[frm-1] = stacks[frm-1][:-count]
            stacks[to-1].extend(to_move)

        answer = ""
        for s in stacks:
            answer += s.pop()
        print("Part2:", answer)
