from enum import Enum
class Direction(Enum):
    NORTH = 1
    SOUTH = 2
    EAST = 3
    WEST = 4

mods = {
    Direction.NORTH: (0, -1),
    Direction.SOUTH: (0, 1),
    Direction.EAST: (1, 0),
    Direction.WEST: (-1, 0)
}

class Diagram:
    def __init__(self, filename):
        self.lines = []
        with open(filename) as f:
            for line in f:
                self.lines.append(line)

    def startingIndex(self):
        return self.lines[0].index('|')

    def outOfBounds(self, x, y):
        return y >= len(self.lines) or x >= len(self.lines[y]) or self.lines[y][x] == ' '

    def newDirection(self, x, y, currentDir):
        if not self.outOfBounds(x, y+1) and currentDir != Direction.NORTH:
            return Direction.SOUTH
        elif not self.outOfBounds(x, y-1) and currentDir != Direction.SOUTH:
            return Direction.NORTH
        if not self.outOfBounds(x+1, y) and currentDir != Direction.WEST:
            return Direction.EAST
        if not self.outOfBounds(x-1, y) and currentDir != Direction.EAST:
            return Direction.WEST
        raise("no valid directions")

#################
    

if __name__ == "__main__":
    #d = Diagram("inputs/test/day19.txt")
    d = Diagram("inputs/day19.txt")

    x = d.startingIndex()
    y = 0


    dir = Direction.SOUTH

    path = ''
    steps = 0

    while True:
        if d.outOfBounds(x, y):
            # finished
            break

        steps += 1

        current = d.lines[y][x]
        if current == "+":    
            # change direction...
            dir = d.newDirection(x, y, dir)
            #print("Direction Change. Now moving: ", dir)

        elif current in ['-', '|']:
            pass
        else:
            #print("passing through: ", current)
            path += current

        (xmod, ymod) = mods[dir]
        x += xmod
        y += ymod

    print("PATH (part1):", path)
    print("steps (part2):", steps)