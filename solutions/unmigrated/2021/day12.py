import copy

class Node:
    def __init__(self, name):
        self.name = name

    def __hash__(self):
        return hash(self.name)

    def __eq__(self, other):
        return self.name == other.name

    def __str__(self):
        return "Node::%s" % self.name

    def __repr__(self) -> str:
        return self.__str__()

    def isStart(self):
        return self.name == "start"
    def isEnd(self):
        return self.name == "end"

    def isSpecial(self):
        return self.isStart() or self.isEnd()
    
    def isSmall(self):
        return ord(self.name[0]) in range(97, 123)

    def isBig(self):
        return ord(self.name[0]) in range(65, 91)

edges = {}

def explore(node, part2, visited=[]):
    if node.name == "end":
        #print(visited, "end")
        return 1

    visited.append(node)
    
    paths = 0
    for neighbor in edges[node]:

        big = neighbor.isBig()

        if big:
            new_visited = copy.copy(visited)
            paths += explore(neighbor, part2, new_visited)
        else:
            if part2:
                if visited.count(neighbor) == 0:
                    new_visited = copy.copy(visited)
                    paths += explore(neighbor, True, new_visited)
                elif visited.count(neighbor) == 1:
                    new_visited = copy.copy(visited)
                    paths += explore(neighbor, False, new_visited)
            else:
                if neighbor not in visited:
                    new_visited = copy.copy(visited)
                    paths += explore(neighbor, False, new_visited)
    return paths



with open("inputs/day12.txt") as f:
    for line in f:
        line = line.strip().split("-")

        a = Node(line[0])
        b = Node(line[1])

        if a not in edges:
            edges[a] = []
        if b not in edges:
            edges[b] = []

        if b.name != "start":
            edges[a].append(b)
        if a.name != "start":
            edges[b].append(a)
    
    print("part1:", explore(Node("start"), False))
    print("part2:", explore(Node("start"), True))

        
