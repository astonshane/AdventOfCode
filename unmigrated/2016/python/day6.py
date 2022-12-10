from collections import Counter

CODE_LENGTH=8

def part1():
    f = open("inputs/day6.txt")

    counts = []

    init = True

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
    print "(part1):", code

def part2():
    f = open("inputs/day6.txt")

    counts = []

    init = True

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
    print "(part2):", code

part2()
