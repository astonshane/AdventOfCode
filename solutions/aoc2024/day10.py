from register import register_solution

def parseInput(filename):
    with open(filename) as f:
        map = []
        for line in f:
            line = [int(x) for x in list(line.strip())]
            map.append(line)
        return map
    
def findTrailheads(map):
    trailheads = []
    for y in range(len(map)):
        for x in range(len(map[y])):
            if map[y][x] == 0:
                trailheads.append((x, y))
    return trailheads

def findNextMoves(map, trailhead):
    (x, y) = trailhead
    moves = []
    if x -1 >= 0 and map[y][x-1] == map[y][x] + 1:
        moves.append((x-1, y))
    if x + 1 < len(map[y]) and map[y][x+1] == map[y][x] + 1:
        moves.append((x+1, y))
    if y -1 >= 0 and map[y-1][x] == map[y][x] + 1:
        moves.append((x, y-1))
    if y + 1 < len(map) and map[y+1][x] == map[y][x] + 1:
        moves.append((x, y+1))
    return moves

def search(map, trailhead) -> set:
    (x, y) = trailhead
    # print(f"searching {trailhead}: {map[y][x]}")
    visited = set()
    visited.add(trailhead)
    if map[y][x] == 9:
        return visited

    possible_next_moves = findNextMoves(map, trailhead)
    for move in possible_next_moves:
        visited = visited.union(search(map, move))
    return visited

def scoreTrail(map, trailhead):
    visited = search(map, trailhead)
    # print(visited)
    score = sum(1 if map[y][x] == 9 else 0 for (x, y) in visited)
    return score

@register_solution(2024, 10, 1)
def part1(filename):
    map = parseInput(filename)
    trailheads = findTrailheads(map)

    total = 0
    for trailhead in trailheads:
        score = scoreTrail(map, trailhead)
        total += score
        print(f"trailhead {trailhead} has score {score}")
    print(f"total score: {total}")

def search2(map, trailhead):
    (x, y) = trailhead
    if map[y][x] == 9:
        return 1
    
    score = 0
    possible_next_moves = findNextMoves(map, trailhead)
    for move in possible_next_moves:
        score += search2(map, move)
    return score


@register_solution(2024, 10, 2)
def part2(filename):
    map = parseInput(filename)
    trailheads = findTrailheads(map)

    total = 0
    for trailhead in trailheads:
        score = search2(map, trailhead)
        total += score
        print(f"trailhead {trailhead} has score {score}")
    print(f"total score: {total}")
