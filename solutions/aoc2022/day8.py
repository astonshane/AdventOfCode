from register import register_solution


def is_visible(x, y, grid):
    # edges
    if min(x, y) == 0 or y == len(grid)-1 or x == len(grid[y])-1:
        return True

    current = grid[y][x]

    # x-axis
    before = grid[y][:x]
    after = grid[y][x+1:]
    if max(before) < current or max(after) < current:
        return True

    # y-axis
    before = [grid[i][x] for i in range(0, len(grid)) if i < y]
    after = [grid[i][x] for i in range(0, len(grid)) if i > y]

    # print(x, y, current)
    # print(before, after)
    if max(before) < current or max(after) < current:
        return True

    return False


@register_solution(2022, 8, 1)
def part1(filename):
    grid = []
    with open(filename) as f:
        for line in f:
            line = line.strip()
            line = [int(x) for x in line]
            grid.append(line)

    visible = 0
    for y in range(0, len(grid)):
        for x in range(0, len(grid[y])):
            if is_visible(x, y, grid):
                visible += 1

    print("part1:", visible)


def scenic_score(x, y, grid):
    # edges
    if min(x, y) == 0 or y == len(grid) - 1 or x == len(grid[y]) - 1:
        return 0

    total_score = 1
    current = grid[y][x]

    # x-axis
    xbefore = grid[y][:x]
    xafter = grid[y][x + 1:]
    #print(x, y, current)
    xbefore.reverse()
    #print(xbefore, xafter)

    # y-axis
    ybefore = [grid[i][x] for i in range(0, len(grid)) if i < y]
    yafter = [grid[i][x] for i in range(0, len(grid)) if i > y]
    ybefore.reverse()
    #print(ybefore, yafter)

    for direction in [xbefore, xafter, ybefore, yafter]:
        score = 0
        for height in direction:
            score += 1
            if height >= current:
                break
        total_score *= score
    return total_score


@register_solution(2022, 8, 2)
def part2(filename):
    grid = []
    with open(filename) as f:
        for line in f:
            line = line.strip()
            line = [int(x) for x in line]
            grid.append(line)

    max_score = 0
    for y in range(0, len(grid)):
        for x in range(0, len(grid[y])):
            max_score = max(max_score, scenic_score(x, y, grid))

    print("part2:", max_score)
