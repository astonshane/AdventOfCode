import sys
from sets import Set

def redistribute(banks):
    index = banks.index(max(banks))
    count = banks[index]
    banks[index] = 0

    while (count > 0):
        index = (index + 1) % len(banks)
        banks[index] += 1
        count -= 1

def part1():
    filename = sys.argv[1]
    with open(filename) as input:
        line = input.read().strip().split("\t")
        banks = [int(x) for x in line]

        seen = Set()
        count = 0
        while (True):
            redistribute(banks)
            count += 1
            banksStr = str(banks)
            if banksStr in seen:
                break
            seen.add(banksStr)
        print "Part1:", count


part1()


def part2():
    filename = sys.argv[1]
    with open(filename) as input:
        line = input.read().strip().split("\t")
        banks = [int(x) for x in line]

        seenOnce = Set()
        seenTwice = {}
        count = 0
        while (True):
            redistribute(banks)
            count += 1
            banksStr = str(banks)
            if banksStr in seenTwice:
                print "Part2:", count - seenTwice[banksStr]
                break
            elif banksStr in seenOnce:
                seenTwice[banksStr] = count
            else:
                seenOnce.add(banksStr)

part2()
