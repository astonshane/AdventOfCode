import re

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
        self.avail = int(m.group(5))
    
    def empty(self):
        return self.used == 0

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

def allViable(all_nodes):
    viable = []
    for a in all_nodes:
        for b in all_nodes:
            if a == b or a.empty():
                continue
            
            if a.used < b.avail:
                viable.append((a, b))
    return viable
            
            

def part1():
    with open("inputs/day22.txt") as f:
        all_nodes = []
        for line in f:
            n = Node(line)
            if n.valid:
                all_nodes.append(n)
        print len(allViable(all_nodes))
        

            


part1()