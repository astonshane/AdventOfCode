import sys
from itertools import combinations

def part1():
    filename = sys.argv[1]
    with open(filename) as input:
        checksum = 0
        for row in input:
            row = row.strip().split("\t")
            row = [int(x) for x in row]
            row.sort()

            checksum += row[-1] - row[0]
        print "Part1():", checksum

def part2():
    filename = sys.argv[1]
    with open(filename) as input:
        checksum = 0
        for row in input:
            row = row.strip().split("\t")
            row = [int(x) for x in row]
            row.sort()

            for combo in combinations(row, 2):
                if combo[1] % combo[0] == 0:
                    checksum += combo[1] / combo[0]
                    break
        print "Part2():", checksum


part2()
