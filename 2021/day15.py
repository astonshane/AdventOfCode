from math import inf
class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.risk = inf

    def __str__(self):
        return "(%d,%d,%f)" % (self.x, self.y, self.risk)

    def __repr__(self):
        return self.__str__()

grid = []
with open("inputs/test/day15.txt") as f:
    for line in f:
        row = [int(x) for x in line.strip()]
        grid.append(row)

print(grid)
depth = len(grid)
width = len(grid[0])

print(depth, width)

visited = set()
unvisited = []
for y in range(0, depth):
    for x in range(0, width):
        unvisited.append(Node(x, y))

n0 = unvisited.pop(0)
n0.risk = 0

total_risk = 0
while len(unvisited) > 0:
    n = unvisited.pop(0)
    print(n)
    if n.x == width-1 and n.y == depth-1:
        print("part1:", total_risk)

    for (a, b) in [(-1,0), (1,0), (0,-1), (0, 1)]:



    unvisited = sorted(unvisited, key=lambda node: node.x)
