from register import register_solution
import re

def checkLine(line, search="XMAS"):
    count = len(re.findall(search, line)) # normal search
    count += len(re.findall(search, line[::-1])) # reverse search
    #print(line, count)
    return count

def diagonal(normal, starting_points, adj):
    count = 0
    for (x, y) in starting_points:
        line = ""
        #print(x, y)
        while (x < len(normal[0]) and y < len(normal)) and (x >= 0 and y >= 0):
            line += normal[y][x]
            y += 1
            x += adj
        count += checkLine(line)
    return count

def rightDiagonal(normal):
    #print("######### right diagonal #########")
    starting_points = []
    for x in range(0, len(normal[0])):
        starting_points.append((x, 0))
    for y in range(1, len(normal)):
        starting_points.append((0, y))

    return diagonal(normal, starting_points, 1)

def leftDiagonal(normal):
    #print("######### left diagonal #########")
    starting_points = []
    for x in range(0, len(normal[0])):
        starting_points.append((x, 0))
    for y in range(1, len(normal)):
        starting_points.append((len(normal)-1, y))

    return diagonal(normal, starting_points, -1)

@register_solution(2024, 4, 1)
def part1(filename):
    count = 0
    normal = []
    with open(filename) as f:
        # normal
        #print("######### normal #########")
        for line in f:
            line = line.strip()
            normal.append(line)
            count += checkLine(line)

    # rotated
    #print("######### rotated #########")
    rotated = []
    for x in range(0, len(normal[0])):
        column = ""
        for line in normal:
            column += line[x]
        rotated.append(column)
        count += checkLine(column)


    count += rightDiagonal(normal)
    count += leftDiagonal(normal)

    print(count)


@register_solution(2024, 4, 2)
def part2(filename):
    count = 0
    normal = []
    with open(filename) as f:
        for line in f:
            line = line.strip()
            normal.append(line)

    for y in range(0, len(normal)):
        for x in range(0, len(normal[0])):
            if y+2 >= len(normal) or x+2 >= len(normal[0]):
                break

            cross1 = normal[y][x] + normal[y+1][x+1] + normal[y+2][x+2]
            cross2 = normal[y+2][x] + normal[y+1][x+1] + normal[y][x+2]
            #print(x, y, cross1, cross2)
            options = ["MAS", "SAM"]
            if cross1 in options and cross2 in options:
                count += 1
    print(count)
