import statistics

class Node:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
        self.count = 0 # how many things are pointing at this node
    def inc(self):
        self.count += 1

nodes = {}
edges = {}

with open("inputs/day7.txt") as f:
    for line in f:
        line = line.strip()
        line = line.split(" -> ")

        node_details = line[0].split()
        name = node_details[0]
        weight = int(node_details[1][1:-1])
        nodes[name] = Node(name, weight)

        if len(line) > 1:
            links = line[1].split(", ")
            edges[name] = links

for name in edges:
    for child in edges[name]:
        nodes[child].inc()

root = None
for name in nodes:
    if nodes[name].count == 0:
        root = name

print("Part1:", root)

def checkBalance(name):
    if name not in edges:
        return nodes[name].weight
    
    children = {}
    for edge in edges[name]:
        children[edge] = checkBalance(edge)
    #print(name, children)

    common_weight = statistics.mode(children.values())
    for child in children:
        if children[child] != common_weight:
            #print(child, children[child], common_weight)
            x = None
            if children[child] > common_weight:
                x = children[child] - common_weight
                nodes[child].weight -= x
            else:
                x = common_weight - children[child]
                nodes[child].weight += x
            print("part2:", nodes[child].weight)
            children[child] = common_weight
            
            

    total_weight = nodes[name].weight
    for x in children.values():
        total_weight += x 
    return total_weight

checkBalance(root)
    
