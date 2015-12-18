import sys
import copy

def countNeighbors(grid, i, j):
    count = 0
    for x in range(-1, 2):
        for y in range(-1, 2):
            ii = i + x
            jj = j + y
            if ii < 0 or jj < 0 or ii >= len(grid) or jj >= len(grid) or (ii == i and jj == j):
                continue
            if grid[ii][jj] == '#':
                count += 1
    return count


def printGrid(grid):
    for row in grid:
        r = ""
        for c in row:
            r += c
        print r
    print ""

def countGrid(grid):
    count = 0
    for row in grid:
        for r in row:
            if r == '#':
                count += 1
    return count

# ######################
if len(sys.argv) != 3:
    print "need an input file and # of steps"
    exit(1)

f = open(sys.argv[1])
steps = int(sys.argv[2])

grid = []
for line in f:
    line = line.strip()
    row = []
    for c in line:
        row.append(c)
    grid.append(row)
# A # means "on", and a . means "off".

print "Initial Grid:"
printGrid(grid)

for step in range(1, steps+1):
    new_grid = copy.deepcopy(grid)
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            count = countNeighbors(grid, i, j)
            if grid[i][j] == '#':
                if count not in [2, 3]:
                    new_grid[i][j] = '.'
            elif grid[i][j] == '.':
                if count == 3:
                    new_grid[i][j] = '#'

    print "After %d steps:" % step
    printGrid(new_grid)
    grid = copy.deepcopy(new_grid)

print "Final number of lights on:", countGrid(grid)
