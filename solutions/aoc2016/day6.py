from register import register_solution
from collections import Counter


@register_solution(2016, 6, 1)
def part1(filename):
    counts = []

    init = True

    with open(filename) as f:
        for line in f:
            line = line.strip()
            for i in range(0, len(line)):
                if init:
                    counts.append(Counter())
                counts[i][line[i]] += 1
            init = False

    code = ""
    for cntr in counts:
        mc = cntr.most_common(1)
        letters = [x[0] for x in mc]
        letters.sort()

        code += letters[0]
    print(code)


@register_solution(2016, 6, 2)
def part2(filename):
    counts = []

    init = True

    with open(filename) as f:
        for line in f:
            line = line.strip()
            for i in range(0, len(line)):
                if init:
                    counts.append(Counter())
                counts[i][line[i]] -= 1
            init = False

    code = ""
    for cntr in counts:
        mc = cntr.most_common(1)
        letters = [x[0] for x in mc]
        letters.sort()

        code += letters[0]
    print(code)
