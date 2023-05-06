from register import register_solution


class Node:
    def __init__(self, letter):
        self.name = letter
        self.dist = None
        self.height = None
        self.visited = False
        if letter == 'S':
            self.height = 0
            # self.dist = 0
        elif letter == 'E':
            self.height = 25
        else:
            self.height = ord(letter) - ord('a')
        self.neighbors = []

    def score(self):
        if self.dist is not None:
            return self.dist + (25-self.height)
        return 25-self.height

    def __str__(self):
        return "%s(%d)" % (self.name, self.score())

    def __repr__(self):
        return self.__str__()

    def reset(self):
        self.dist = None
        self.visited = False


def parse_input(filename):
    grid = []
    with open(filename) as f:
        for line in f:
            grid.append([Node(x) for x in list(line.strip())])

    s = None
    length = len(grid)
    for i in range(0, length):
        width = len(grid[i])
        for j in range(0, width):
            n = grid[i][j]
            if n.name == 'S':
                s = n
            max_height = n.height + 1

            if j - 1 >= 0 and grid[i][j-1].height <= max_height:
                n.neighbors.append(grid[i][j-1])
            if j + 1 < width and grid[i][j + 1].height <= max_height:
                n.neighbors.append(grid[i][j + 1])
            if i - 1 >= 0 and grid[i-1][j].height <= max_height:
                n.neighbors.append(grid[i-1][j])
            if i + 1 < length and grid[i + 1][j].height <= max_height:
                n.neighbors.append(grid[i + 1][j])

    return grid, s


def a_star(s, grid):
    for row in grid:
        for node in row:
            node.reset()
    s.dist = 0

    q = [s]
    while len(q) > 0:
        q.sort(key=lambda x: x.score())
        # print(q)
        current = q.pop(0)
        if current.visited:
            continue
        # print(current)

        if current.name == 'E':
            print("Found E in %d moves" % current.dist)
            return current.dist

        current.visited = True
        # print(current, current.neighbors)
        for neighbor in current.neighbors:
            new_dist = current.dist + 1
            if neighbor.dist is None or new_dist < neighbor.dist:
                neighbor.dist = new_dist
                q.append(neighbor)


@register_solution(2022, 12, 1)
def part1(filename):
    grid, s = parse_input(filename)
    print("part1:", a_star(s, grid))


@register_solution(2022, 12, 2)
def part2(filename):
    grid, s = parse_input(filename)
    print("# nodes:", len(grid)*len(grid[0]))
    possible_starts = []
    for row in grid:
        for node in row:
            if node.name == 'a':
                possible_starts.append(node)
    print(len(possible_starts))

    distances = []
    for node in possible_starts:
        dist = a_star(node, grid)
        if dist is not None:
            distances.append(dist)
    print(min(distances))
