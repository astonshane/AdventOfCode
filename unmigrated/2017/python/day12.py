
edges = {}
visited = set()

def visit(x):
    visits = 1
    visited.add(x)
    for n in edges[x]:
        if n not in visited:
            visits += visit(n)
    return visits

with open("inputs/day12.txt") as f:
    for line in f:
        [source, dests] = line.strip().split(" <-> ")
        dests = dests.split(", ")
        edges[source] = dests

    groups = 0
    for x in edges:
        if x in visited:
            continue
        groups += 1
        visits = visit(x)
        if x == "0":
            print("part1:", visits)
    print("part2:", groups)
