import operator
from functools import reduce

def get(caves, i, j):
    if i < 0 or i >= len(caves):
        return None
    if j < 0 or j >= len(caves[i]):
        return None
    return caves[i][j]


modifiers = [
    (-1, 0),
    (1, 0),
    (0, -1),
    (0, +1)
]

with open("inputs/day9.txt") as f:
    caves = []
    for line in f:
        caves.append([int(x) for x in line.strip()])
    total_risk = 0

    for i in range(0, len(caves)):
        for j in range(0, len(caves[i])):
            #print(i, j, caves[i][j])
            val = caves[i][j]

            surrounding = []
            for (a,b) in modifiers:
                x = get(caves, i+a, j+b)
                if x is not None:
                    surrounding.append(x)
            if min(surrounding) > val:
                risk = 1 + val
                total_risk += risk

    print("part1:", total_risk)

def visit(caves, i, j):
    #print("visiting %d,%d" % (i,j))
    count = 1
    caves[i][j] = 'V'
    for (a,b) in modifiers:
        x = get(caves, i+a, j+b)
        if x not in [None, 9, 'V']:
            #print(x)
            count += visit(caves, i+a, j+b)
    return count


def printCaves(caves):
    print('#'*len(caves[0]))
    for i in range(0, len(caves)):
        print(''.join([str(x) for x in caves[i]]))
    print('#'*len(caves[0]))

with open("inputs/day9.txt") as f:
    caves = []
    for line in f:
        caves.append([int(x) for x in line.strip()])

    #printCaves(caves)
    basins = []

    for i in range(0, len(caves)):
        for j in range(0, len(caves[i])):
            val = caves[i][j]
            if val in [9, 'V']:
                continue

            size = visit(caves, i, j)
            #print("Basin of size:", size)
            basins.append(size)
            #printCaves(caves)
    
    basins.sort()
    #print(basins)

    prod = reduce(operator.mul, basins[-3:], 1)
    print("part2:", prod)

