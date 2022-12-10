def findEdges(dots):
    mx = 0
    my = 0

    for (x,y) in dots:
        mx = max(mx, x)
        my = max(my, y)

    return mx+1, my+1

class Grid:
    def __init__(self, max_x, max_y):
        self.grid = []
        for x in range(0, max_y):
            row = [False]*max_x
            self.grid.append(row)

    def print(self):
        print("##########start##########")
        for row in self.grid:
            #print(row)
            tmp = ['#' if x else '.' for x in row]
            print(''.join(tmp))
        print("##########end############")

    def readDots(self, dots):
        for (x,y) in dots:
            self.grid[y][x] = True

    def split(self, direction, location):
        other = Grid(0,0)

        if direction == 'x':
            other.grid = []
            for i in range(0, len(self.grid)):
                other.grid.append(self.grid[i][location+1:])
                self.grid[i] = self.grid[i][:location]
        else:
            other.grid = self.grid[location+1:]
            self.grid = self.grid[:location]

        return other

    def flip(self, direction):
        if direction == 'x':
            for i in range(0, len(self.grid)):
                self.grid[i].reverse()
        else:
            self.grid.reverse()


    def merge(self, other):
        # ensure the 'self' grid is big enough for uneven folds
        for i in range(0, len(self.grid)):
            while len(self.grid[i]) < len(other.grid[0]):
                self.grid[i].insert(0, False)
        while len(self.grid) < len(other.grid):
            self.grid.insert(0, [False]*len(other.grid[0]))

        # ensure the 'other' grid is big enough for uneven folds
        for i in range(0, len(other.grid)):
            while len(other.grid[i]) < len(self.grid[0]):
                other.grid[i].insert(0, False)
        while len(other.grid) < len(self.grid):
            other.grid.insert(0, [False]*len(self.grid[0]))

        # merge
        for i in range(0, len(self.grid)):
            for j in range(0, len(self.grid[i])):
                self.grid[i][j] = self.grid[i][j] or other.grid[i][j]

    def count(self):
        count = 0
        for i in range(0, len(self.grid)):
            for j in range(0, len(self.grid[i])):
                if self.grid[i][j]:
                    count += 1
        return count




lines = []
with open("inputs/day13.txt") as f:
    lines = f.readlines()

brk = lines.index("\n")

dots = [x.strip().split(",") for x in lines[:brk]]
dots = [(int(a), int(b)) for [a,b] in dots]

instructions = [x.strip().split()[2].split('=') for x in lines[brk+1:]]
instructions = [(a, int(b)) for [a,b] in instructions]

#print(dots)
#print(instructions)

MAX_X, MAX_Y = findEdges(dots)

grid = Grid(MAX_X, MAX_Y)
grid.readDots(dots)

for (direction, location) in instructions:
    grid2 = grid.split(direction, location)

    #print("grid1")
    grid.print()
    #print("grid2:")
    #grid2.print()
    grid2.flip(direction)
    #print("grid2 flipped:")
    #grid2.print()
    grid.merge(grid2)
    #print("merged:")
    #grid.print()
    #print(grid.count())
    #break

grid.print()
