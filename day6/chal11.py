import copy

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


# initilize grid
row = []
for i in range(0, 1000):
    row.append(False)

grid = []
for i in range(0, 1000):
    grid.append(copy.deepcopy(row))

# read in file
f = open("chal11_input.txt")

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

print countOn(grid)
