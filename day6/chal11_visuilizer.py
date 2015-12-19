import copy
import os
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
def toInt(cmd):
    cmd[0] = int(cmd[0])
    cmd[1] = int(cmd[1])
    return cmd


def countOn(grid):
    count = 0
    for i in range(0, 1000):
        for j in range(0, 1000):
            if grid[j][i]:
                count = count + 1
    return count

def generateImage(grid, id):
    size = (len(grid), len(grid))
    img = Image.new('RGB', size, 'black')
    pixels = img.load()
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if grid[i][j]:
                pixels[i,j] = (i, j, 100)
    draw = ImageDraw.Draw(img)
    draw.text((5, 5), str(id), fill=(255, 255, 0))
    id = str(id)
    if len(id) != 3:
        id = "0"*(3 - len(id) % 3)+id
    img.save("tmp/%s.png" % (id))
# initilize grid
row = []
for i in range(0, 1000):
    row.append(False)

grid = []
for i in range(0, 1000):
    grid.append(copy.deepcopy(row))


os.system("rm tmp/*.png")


# read in file
f = open("chal11_input.txt")
count = 0
for line in f:
    cmd = line.strip().split(' ')
    print cmd
    if cmd[0] == "toggle":
        start = toInt(cmd[1].split(","))
        end = toInt(cmd[3].split(","))
        print "toggling...", start, end
        for i in range(start[0], end[0]+1):
            for j in range(start[1], end[1]+1):
                grid[j][i] = not grid[j][i]
    else:
        start = toInt(cmd[2].split(","))
        end = toInt(cmd[4].split(","))
        if cmd[1] == "on":
            print "turning on...", start, end
            for i in range(start[0], end[0]+1):
                for j in range(start[1], end[1]+1):
                    grid[j][i] = True


        elif cmd[1] == "off":
            print "turning off...", start, end
            for i in range(start[0], end[0]+1):
                for j in range(start[1], end[1]+1):
                    grid[j][i] = False

    generateImage(grid, count)
    count += 1

print countOn(grid)
os.system("convert -loop 0 -delay 25 tmp/*.png animation.gif")
# os.system("rm tmp/*.png")
