import sys
import time
import copy

class Node:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
        self.children = []

    def __str__(self):
        return "%s -> %s" % (self.name, str(self.children))

    def __repr__(self):
        return self.__str__();

def calcWeight(node):
    sum = node.weight
    for child in node.children:
        sum += calcWeight(child)
    return sum

def findMisweighted(node, goal):
    #print "starting", node.name, node.weight, goal
    if len(node.children) == 0:
        print "GOAL!!", goal

    weights = {}
    for child in node.children:
        #print "visisting", child.name
        weight = calcWeight(child)
        weights[weight] = weights.get(weight, [])
        weights[weight].append(child)

    nxt = None
    newGoal = 0
    #print weights
    for weight in weights:
        if len(weights[weight]) == 1:
            nxt = weights[weight][0]
        else:
            newGoal = weight
    if nxt is None:
        # I'm the problem!
        print "GOAL!", abs(goal - newGoal*len(weights[newGoal]))
    else:
        #print "child", nxt
        findMisweighted(nxt, newGoal)




filename = sys.argv[1]
with open(filename) as input:
    nodeMap = {}

    for line in input:
        line = line.strip().split(" ", 3)
        name = line[0]
        n = Node(name, int(line[1][1:-1]))
        if len(line) > 2:
            n.children = line[3].split(", ")
        nodeMap[name] = n



    for name in nodeMap:
        node = nodeMap[name]
        node.children = [nodeMap[x] for x in node.children]

    #for name in nodeMap:
    #    print nodeMap[name]

    lengths = [len(nodeMap[x].__str__()) for x in nodeMap]
    root = nodeMap.keys()[lengths.index(max(lengths))]
    print "Part1():", root

    root = nodeMap[root]

    findMisweighted(root, 0)
