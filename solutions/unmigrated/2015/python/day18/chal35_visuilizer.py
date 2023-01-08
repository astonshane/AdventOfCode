import sys
import copy
import os
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont


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


def printGrid(grid, id=0):
    size = (len(grid), len(grid))
    img = Image.new('RGB', size, 'black')
    pixels = img.load()
    for i in range(0, len(grid)):
        for j in range(0, len(grid)):
            if grid[i][j] == '#':
                pixels[i, j] = (i, j, 100)
    draw = ImageDraw.Draw(img)
    draw.text((5, 5), str(id), fill=(255, 255, 0))
    id = str(id)
    if len(id) != 3:
        id = "0"*(3 - len(id) % 3)+id
    img.save("tmp/%s.png" % (id))


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

os.system("rm tmp/*.png")

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

    grid = copy.deepcopy(new_grid)
    printGrid(grid, step)

os.system("convert -dispose background -delay 50 -loop 1 tmp/*.png animation.gif")
os.system("rm tmp/*.png")
