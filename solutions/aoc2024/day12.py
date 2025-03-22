from register import register_solution

def parseInput(filename):
    with open(filename) as f:
        garden = []
        for line in f:
            line = line.strip()
            # print(line)
            garden.append(list(line))
        return garden
    
def search(garden, x, y, visited) -> set:
    visited.add((x, y))
    current_val = garden[y][x]

    region = set()
    region.add((x, y))

    if y - 1 >= 0 and garden[y-1][x] == current_val and (x, y-1) not in visited:
        region = region.union(search(garden, x, y-1, visited))

    if y + 1 < len(garden) and garden[y+1][x] == current_val and (x, y+1) not in visited:
        region = region.union(search(garden, x, y+1, visited))

    if x - 1 >= 0 and garden[y][x-1] == current_val and (x-1, y) not in visited:
        region = region.union(search(garden, x-1, y, visited))

    if x + 1 < len(garden[y]) and garden[y][x+1] == current_val and (x+1, y) not in visited:
        region = region.union(search(garden, x+1, y, visited))
    
    return region

def scoreRegion(region, garden):
    perimeter = 0
    for (x, y) in region:
        val = garden[y][x]
        if y - 1 < 0 or garden[y-1][x] != val:
            perimeter += 1
        if y + 1 >= len(garden) or garden[y+1][x] != val:
            perimeter += 1
        if x - 1 < 0 or garden[y][x-1] != val:
            perimeter += 1
        if x + 1 >= len(garden[y]) or garden[y][x+1] != val:
            perimeter += 1
    area = len(region)
    return area * perimeter

@register_solution(2024, 12, 1)
def part1(filename):
    garden = parseInput(filename)

    total = 0
    
    visited = set()
    for y in range(0, len(garden)):
        for x in range(0, len(garden[y])):
            if (x, y) not in visited:
                region = search(garden, x, y, visited)
                # print(f"found {garden[y][x]} region {region}")
                score = scoreRegion(region, garden)
                total += score
                # print(f"scored {score}")
    print(total)

def getNode(garden, x, y):
    if y < 0 or y >= len(garden) or x < 0 or x >= len(garden[y]):
        return None
    return garden[y][x]

def scoreRegion2(region, garden):
    sides = 0
    # corners == sides
    for (x, y) in region:
        val = garden[y][x]
        node_corners = 0

        current = getNode(garden, x, y)
        
        left = getNode(garden, x-1, y)
        right = getNode(garden, x+1, y)
        up = getNode(garden, x, y-1)
        down = getNode(garden, x, y+1)

        if current != left and current != up:
            node_corners += 1
        if current != right and current != up:
            node_corners += 1
        
        if current != left and current != down:
            node_corners += 1
        if current != right and current != down:
            node_corners += 1

        if current == right and current == down and current != getNode(garden, x+1, y+1):
            node_corners += 1
        if current == right and current == up and current != getNode(garden, x+1, y-1):
            node_corners += 1
        if current == left and current == down and current != getNode(garden, x-1, y+1):
            node_corners += 1
        if current == left and current == up and current != getNode(garden, x-1, y-1):
            node_corners += 1


        # print(f"node {x},{y} has {node_corners} corners")
        sides += node_corners

    # print(f"region {region} ({len(region)}) has {sides} sides")

    return sides * len(region)

@register_solution(2024, 12, 2)
def part2(filename):
    garden = parseInput(filename)

    total = 0
    
    visited = set()
    for y in range(0, len(garden)):
        for x in range(0, len(garden[y])):
            if (x, y) not in visited:
                region = search(garden, x, y, visited)
                # print(f"found {garden[y][x]} region {region}")
                score = scoreRegion2(region, garden)
                total += score
                # print(f"scored {score}")
    print(total)
