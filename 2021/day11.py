transforms = [
    (1,0),
    (-1,0),
    (0,1),
    (0,-1),
    (-1,-1),
    (-1,1),
    (1,1),
    (1,-1)
]

class Grid:
    def __init__(self, filename):
        self.flashes = 0
        with open(filename) as f:
            self.grid = []
            for line in f:
                line = line.strip()
                line = [int(x) for x in line]
                self.grid.append(line)

    def validCoord(self, i, j):
        return (i >= 0) and (i < len(self.grid))  and (j >= 0) and (j < len(self.grid[i]))

    def print(self):
        for line in self.grid:
            print(''.join([str(x) for x in line]))
        print("#####")

    def step(self):
        # first, the energy level of each octopus increaes by 1
        for i in range(0, len(self.grid)):
            for j in range(0, len(self.grid[i])):
                self.grid[i][j] += 1

        flashed = set()

        to_process = []

        # then any with a level > 9 flashes
        for i in range(0, len(self.grid)):
            for j in range(0, len(self.grid[i])):
                to_process.append((i,j))

        while len(to_process) > 0:
            (i,j) = to_process.pop(0)
            if self.grid[i][j] > 9:
                #print(i,j)
                self.flashes += 1
                flashed.add((i,j))
                for (a,b) in transforms:
                    x = i+a
                    y = j+b
                    if self.validCoord(x, y):
                        self.grid[x][y] += 1
                        if (x,y) not in flashed and (x,y) not in to_process:
                            to_process.append((x,y))
                

        
        for (i,j) in flashed:
            self.grid[i][j] = 0

        if len(flashed) == (len(self.grid) * len(self.grid[0])):
            return True # found part two - stop processing
        return False # continue processing

grid = Grid("inputs/day11.txt")
#grid.print() 
flashes = 0

step = 0

stop = False

while not stop:
    step += 1
    stop = grid.step()
    #print("after step", i+1)
    #grid.print() 
    if step == 100:
        print("part1:", grid.flashes)

print("part2:", step)
#grid.print()