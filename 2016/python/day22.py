import re
import copy
import hashlib

class Node:
    def __init__(self, line):
        m = re.match(r"\/dev\/grid\/node-x(\d+)-y(\d+)\s+(\d+)T\s+(\d+)T\s+(\d+)T\s+(\d+)%", line)
        if m is None:
            self.valid = False
            return

        self.valid = True
        self.x = int(m.group(1))
        self.y = int(m.group(2))
        self.size = int(m.group(3))
        self.used = int(m.group(4))

        self.goal = False

    def avail(self):
        return self.size - self.used
    
    def empty(self):
        return self.used == 0

    def start(self):
        return self.x == 0 and self.y == 0

    def __str__(self):
        return "(%d, %d)" % (self.x, self.y)

    def __repr__(self):
        return self.__str__()

    def __cmp__(self, other):
        c = self.x - other.x
        if c == 0:
            return self.y - other.y
        return c

    def __ne__(self, other):
        return not self.__eq__(other) 

def part1():
    with open("inputs/day22.txt") as f:
        all_nodes = []
        for line in f:
            n = Node(line)
            if n.valid:
                all_nodes.append(n)
       
        viable = []
        for a in all_nodes:
            for b in all_nodes:
                if a == b or a.empty():
                    continue
                
                if a.used < b.avail():
                    viable.append((a, b))
        print "Part1:", len(viable)


class Grid:
    def __init__(self, filename):
        self.grid = {}
        self.goal = None
        self.emptyNode = None
        self.steps = 0

        with open(filename) as f:
            for line in f:
                n = Node(line)
                if n.valid:
                    self.grid[str(n)] = n
                    if (self.goal is None):
                        n.goal = True
                        self.goal = n
                    elif (n.y == 0) and n.x > self.goal.x:
                        self.goal.goal = False
                        n.goal = True
                        self.goal = n
                    if n.empty():
                        self.emptyNode = n

    def getHome(self):
        return self.get("(0, 0)")

    def get(self, s):
        return self.grid.get(s, None)

    def set(self, s, val):
        self.grid[s] = val
    
    def __str__(self):
        return str(self.grid)

    def __repr__(self):
        return self.__str__()

    def hash(self):
        m = hashlib.md5()
        for key in self.grid:
            node = self.grid[key]
            m.update("(%d,%d,%d,%d)" % (node.x, node.y, node.size, node.used))
        return m.digest()

    def draw(self):
        print "######################\n"
        y = 0
        broken = 0
        while True:
            x = 0
            while True:
                n = self.get("(%d, %d)" % (x, y))
                if n is not None:
                    broken = 0

                    c = None
                    if n.goal:
                        c = "G"
                    elif n.empty():
                        c = "_"
                    else:
                        c = "."
                    
                    if n.start():
                        print "(%s)" % c,
                    else:
                        print " %s " % c,
                else:
                    broken += 1
                    print ""
                    break
                x += 1
            if broken == 2:
                break
            y += 1
            

        print "######################"


def bfs(grid_list, steps=0, duplicates=[]):
    if len(grid_list) == 0:
        return -1
    
    print "========================================="
    print "BFS(%d): %d" % (steps, len(grid_list))
    
    next_grids = []
    for baseGrid in grid_list:
        homeNode = baseGrid.getHome()
        if homeNode.empty() and (baseGrid.get("(1, 0)").goal or baseGrid.get("(0, 1)").goal):
            return steps+1
        
        for (x, y) in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            grid = copy.deepcopy(baseGrid)
            empty = grid.emptyNode
            nxt_str = "(%d, %d)" % (empty.x+x, empty.y+y)
            nxt = grid.get(nxt_str)

            if (nxt is not None) and (empty.size >= nxt.used):
                empty.used = nxt.used
                nxt.used = 0
                if nxt.goal:
                    nxt.goal = False
                    empty.goal = True
                grid.emptyNode = nxt

            hsh = grid.hash()
            if hsh not in duplicates:
                duplicates.append(hsh)
                next_grids.append(grid)

    return bfs(next_grids, steps+1, duplicates)
            

def part2():
    # this solution works for the sample data, but takes *forever* on the given data
    # ended up using https://codepen.io/anon/pen/BQEZzK to come up with the final anser
    grid = Grid("inputs/test.txt")
    print "shortest: %d" % bfs([grid])
    #grid.draw()

#part1()
part2()