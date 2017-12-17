import sys
from itertools import combinations
from sets import Set

def part1():
    filename = sys.argv[1]
    with open(filename) as input:
        valid = 0
        for line in input:
            line = line.strip().split(" ")
            before = len(line)
            line = set(line)
            after = len(line)

            if before == after:
                valid += 1
        print "Part1:", valid
part1()

def part2():
    filename = sys.argv[1]
    with open(filename) as input:
        valid = 0
        for line in input:
            line = line.strip().split(" ")
            before = len(line)

            lineSet = Set()
            for w in line:
                lineSet.add(''.join(sorted(w)))

            after = len(lineSet)

            if before == after:
                valid += 1
        print "Part2:", valid
part2()
