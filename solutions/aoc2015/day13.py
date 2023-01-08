from register import register_solution
import itertools


def parseFile(filename):
    hUnits = {}
    with open(filename) as f:
        for line in f:
            line = line.strip(" \n.").split()
            person1 = line[0]
            person2 = line[-1]
            units = int(line[3])
            if line[2] == 'lose':
                units *= -1

            if person1 not in hUnits:
                hUnits[person1] = {}
            hUnits[person1][person2] = units
    return hUnits


def findHappiness(arrangement, hUnits):
    happiness = 0
    for i in range(0, len(arrangement)):
        person = arrangement[i]
        personLeft, personRight = None, None
        if i == 0:
            personLeft = arrangement[-1]
        else:
            personLeft = arrangement[i - 1]

        if i == len(arrangement) - 1:
            personRight = arrangement[0]
        else:
            personRight = arrangement[i + 1]

        happiness += hUnits[person][personLeft] + hUnits[person][personRight]
    return happiness


@register_solution(2015, 13, 1)
def part1(filename):
    hUnits = parseFile(filename)
    max_happy = None
    allPerms = itertools.permutations(hUnits.keys())
    for perm in allPerms:
        tmp = findHappiness(perm, hUnits)
        if max_happy is None or tmp > max_happy:
            max_happy = tmp

    print("max_happiness:", max_happy)


@register_solution(2015, 13, 2)
def part2(filename):
    hUnits = parseFile(filename)
    # add 'me' to the list
    users = hUnits.keys()
    hUnits['me'] = {}
    for user in users:
        hUnits['me'][user] = 0
        hUnits[user]['me'] = 0

    max_happy = None
    allPerms = itertools.permutations(hUnits.keys())
    for perm in allPerms:
        tmp = findHappiness(perm, hUnits)
        if max_happy is None or tmp > max_happy:
            max_happy = tmp

    print("max_happiness:", max_happy)
