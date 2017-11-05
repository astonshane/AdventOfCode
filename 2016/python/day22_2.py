import re
from sets import Set
from Queue import Queue, PriorityQueue
class Node:
    symbol = '.'
    def __init__(self, args):
        args = [int(x) for x in args]
        self.x = args[0]
        self.y = args[1]
        self.size = args[2]
        self.used = args[3]
        self.avail = args[4]
        self.usePct = args[5]

    def getPos(self):
        return (self.x, self.y)

    def rep(self):
        return "(%d:%s)" % (self.used, self.symbol)

    def __str__(self):
        return self.symbol
        # return "(%d, %d)" % (self.x, self.y)

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return (self.x, self.y) == (other.x, other.y)
        return NotImplemented

    def __ne__(self, other):
        if isinstance(other, self.__class__):
            return not self.__eq__(other)
        return NotImplemented

def printGrid(grid):
    print ""
    for row in grid:
        for node in row:
            print node,
        print ""

def repGrid(grid):
    grd = ""
    for row in grid:
        for node in row:
            grd += node
    return grd

MAX_X = 36
MAX_Y = 26
LIMIT = 100
filename = "inputs/day22.txt"

grid = []
for i in range(0, MAX_Y+1):
    row = [None]*(MAX_X+1)
    grid.append(row)

with open(filename) as f:
    for line in f:
        line = line.strip()
        r = '/dev/grid/node-x(\d+)-y(\d+)\s+(\d+)T\s+(\d+)T\s+(\d+)T\s+(\d+)\%'
        m = re.match(r, line)
        if m is not None:
            node = Node(m.groups())
            if node.x == 0 and node.y == 0:
                node.symbol = "&"
            elif node.y == 0 and node.x == MAX_X:
                node.symbol = "G"
            elif node.size > LIMIT:
                node.symbol = "#"
            elif node.used == 0:
                node.symbol = "_"
            grid[node.y][node.x] = node.symbol

printGrid(grid)
pQueue = PriorityQueue()
