import re
import itertools
from copy import deepcopy
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

def viable(a, b):
    #print "%s.used(%d) > 0:" % (str(a), a.used), a.used > 0
    #print "%s.used < %s.used == %d < %d" % (a, b, a.used, b.avail), a.used < b.avail
    if a != b and a.used > 0 and a.used < b.avail and a.symbol != "#":
        return True
    return False

def part1():
    nodes = []
    with open("inputs/day22.txt") as f:
        for line in f:
            line = line.strip()
            r = '/dev/grid/node-x(\d+)-y(\d+)\s+(\d+)T\s+(\d+)T\s+(\d+)T\s+(\d+)\%'
            m = re.match(r, line)
            if m is not None:
                nodes.append(Node(m.groups()))

    viables = 0
    considered = 0
    for combo in itertools.permutations(nodes, 2):
        considered += 1
        if viable(combo[0], combo[1]):
            viables += 1

    print "(part1):", viables

def printGrid(grid):
    print ""
    for row in grid:
        for node in row:
            print node,
        print ""

def gridHash(grid):
    rep = ""
    for row in grid:
        for node in row:
            rep += node.rep()
    return rep

def findEmpty(grid):
    for row in grid:
        for node in row:
            if node.used == 0:
                return node.x, node.y
    return -1, -1


MAX_X = 36
MAX_Y = 26
LIMIT = 100
filename = "inputs/day22.txt"


'''
MAX_X = 2
MAX_Y = 2
LIMIT = 20
filename = "inputs/test.txt"
'''

def dist(grid, toStart=False):
    goalX, goalY = None, None
    if toStart:
        goalX, goalY = 0, 0
    else:
        goalX, goalY = MAX_X, 0
    emptyX, emptyY = findEmpty(grid)
    return abs(goalX - emptyX) + abs(goalY - emptyY)

def part2():
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
                grid[node.y][node.x] = node

    TO_START = False

    printGrid(grid)
    states = Set()
    states.add(gridHash(grid))

    pQueue = PriorityQueue()
    pQueue.put((dist(grid, TO_START), grid, 0))

    while not pQueue.empty():
        print pQueue.qsize()
        g = pQueue.get()
        if g[0] == 0:
            if TO_START:
                print "solved in %d steps" % g[2]
                printGrid(grid)
                break
            else:
                TO_START = True
                pQueue = PriorityQueue()

        grid = g[1]
        emptyX, emptyY = findEmpty(grid)
        printGrid(grid)
        raw_input()
        #print emptyX, emptyY

        # move x
        for i in [-1, 1]:
            newGrid = deepcopy(grid)
            newEmptyX = emptyX + i
            if newEmptyX >= 0 and newEmptyX <= MAX_X and viable(newGrid[emptyY][newEmptyX], newGrid[emptyY][emptyX]):
                newGrid[emptyY][emptyX].used = newGrid[emptyY][newEmptyX].used
                newGrid[emptyY][emptyX].avail = newGrid[emptyY][emptyX].size - newGrid[emptyY][emptyX].used
                newGrid[emptyY][emptyX].symbol = newGrid[emptyY][newEmptyX].symbol

                newGrid[emptyY][newEmptyX].symbol = "_"
                newGrid[emptyY][newEmptyX].used = 0
                newGrid[emptyY][newEmptyX].avail = newGrid[emptyY][newEmptyX].size

                hsh = gridHash(newGrid)
                if hsh not in states:
                    states.add(hsh)
                    pQueue.put((dist(newGrid, TO_START), newGrid, g[2]+1))

        for j in [-1, 1]:
            newGrid = deepcopy(grid)
            newEmptyY = emptyY + j
            if newEmptyY >= 0 and newEmptyY <= MAX_Y and viable(newGrid[newEmptyY][emptyX], newGrid[emptyY][emptyX]):
                newGrid[emptyY][emptyX].used = newGrid[newEmptyY][emptyX].used
                newGrid[emptyY][emptyX].avail = newGrid[emptyY][emptyX].size - newGrid[emptyY][emptyX].used
                newGrid[emptyY][emptyX].symbol = newGrid[newEmptyY][emptyX].symbol

                newGrid[newEmptyY][emptyX].symbol = "_"
                newGrid[newEmptyY][emptyX].used = 0
                newGrid[newEmptyY][emptyX].avail = newGrid[newEmptyY][emptyX].size

                hsh = gridHash(newGrid)
                if hsh not in states:
                    states.add(hsh)
                    pQueue.put((dist(newGrid, TO_START), newGrid, g[2]+1))


#part1()
part2()
