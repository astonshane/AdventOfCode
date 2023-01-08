from register import register_solution
from itertools import combinations


def getContainers(filename):
    containers = []
    with open(filename) as f:
        for line in f:
            containers.append(int(line.strip()))
    return containers


def sumCombo(combo):
    total = 0
    for i in combo:
        total += i
    return total

@register_solution(2015, 17, 1)
def part1(filename):
    storage = 150
    containers = getContainers(filename)
    total_combos = 0

    for i in range(0, len(containers)):
        for combo in combinations(containers, i):
            if sumCombo(combo) == storage:
                total_combos += 1

    print(total_combos)


@register_solution(2015, 17, 2)
def part2(filename):
    storage = 150
    containers = getContainers(filename)

    total_combos = None
    combo_length = None

    for i in range(0, len(containers)):
        for combo in combinations(containers, i):
            if sumCombo(combo) == storage:
                if combo_length is None or len(combo) < combo_length:
                    total_combos = 1
                    combo_length = len(combo)
                elif len(combo) == combo_length:
                    total_combos += 1

    print(combo_length, total_combos)

