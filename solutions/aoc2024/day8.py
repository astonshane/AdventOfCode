from register import register_solution
from itertools import combinations

def parseInput(filename):
    with open(filename) as f:
        locations = {}

        board = []
        for line in f:
            line = line.strip()
            board.append(line)
        
        for y in range(0, len(board)):
            for x in range(0, len(board[0])):
                if board[y][x] not in ['.', '#']:
                    if board[y][x] not in locations:
                        locations[board[y][x]] = []
                    locations[board[y][x]].append((x, y))
        return locations, len(board[0]), len(board), board
    
def calculateDistance(location1, location2):
    return location1[0] - location2[0], location1[1] - location2[1]

def generateAntinodes(location1, location2):
    x_dist, y_dist = calculateDistance(location1, location2)

    antinodes = []
    if (location1[0] + x_dist, location1[1] + y_dist) == location2:
        antinodes.append((location1[0] - x_dist, location1[1] - y_dist))
        antinodes.append((location1[0] + x_dist*2, location1[1] + y_dist*2))
    else:
        antinodes.append((location2[0] - x_dist, location2[1] - y_dist))
        antinodes.append((location2[0] + x_dist*2, location2[1] + y_dist*2))
    return antinodes

def validateAntinode(antinode, width, height):
    return antinode[0] >= 0 and antinode[0] < width and antinode[1] >= 0 and antinode[1] < height
    
@register_solution(2024, 8, 1)
def part1(filename):
    locations, width, height, board = parseInput(filename)
    # print(locations, width, height)

    antinode_locations = set()
    for frequency in locations:
        for combo in combinations(locations[frequency], 2):
            antenna1 = combo[0]
            antenna2 = combo[1]

            possible_antinodes = generateAntinodes(antenna1, antenna2)
            for antinode in possible_antinodes:
                if validateAntinode(antinode, width, height):
                    antinode_locations.add(antinode)
    print(f"# Antinodes: {len(antinode_locations)}")
    # print(antinode_locations)

    # # verify antinodes:
    # for antinode in antinode_locations:
    #     print(antinode, board[antinode[1]][antinode[0]])
    #     if board[antinode[1]][antinode[0]] != '#':
    #         print("failure!")


@register_solution(2024, 8, 2)
def part2(filename):
    locations, width, height, board = parseInput(filename)

    antinode_locations = set()
    for frequency in locations:
        for combo in combinations(locations[frequency], 2):
            antenna1 = combo[0]
            antenna2 = combo[1]

            x_dist, y_dist = calculateDistance(antenna1, antenna2)

            # up and to left
            new_antinode = (antenna1[0], antenna1[1])
            while(validateAntinode(new_antinode, width, height)):
                antinode_locations.add(new_antinode)
                new_antinode = (new_antinode[0] - x_dist, new_antinode[1] - y_dist)

            # down and to right
            new_antinode = (antenna2[0], antenna2[1])
            while(validateAntinode(new_antinode, width, height)):
                antinode_locations.add(new_antinode)
                new_antinode = (new_antinode[0] + x_dist, new_antinode[1] + y_dist)
    print(f"# Antinodes: {len(antinode_locations)}")


