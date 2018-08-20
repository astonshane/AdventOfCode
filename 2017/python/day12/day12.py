from sets import Set

def contained(edges, node, s):
    if node not in s:
        s.add(node)
        for n in edges[node]:
            s = s.union(contained(edges, n, s))
    return s

def part1(edges):
        group = contained(edges, 0, Set())
        print "part1:", len(group)

def part2(edges):
        keys = Set(edges.keys())
        groups = 0
        while len(keys) > 0:
            groups += 1
            key = keys.pop()
            group = contained(edges, key, Set())
            keys = keys.difference(group)
        print "Part2:", groups

with open("input.txt") as f:
    edges = {}
    for line in f:
        [node, neighbors] = line.strip().split(" <-> ")
        neighbors = [int(x) for x in neighbors.split(", ")]
        edges[int(node)] = neighbors

    part1(edges)
    part2(edges)