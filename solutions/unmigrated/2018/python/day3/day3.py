class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.claims = []

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return str(self.claims)

grid = {}

with open("input.txt") as f:
    for line in f:
        line = line.strip().split()
        claimer = line[0][1:]
        start = [int(x) for x in line[2][:-1].split(",")]
        size = [int(x) for x in line[3].split("x")]

        for y in range(0, size[1]):
            for x in range(0, size[0]):
                x_idx = start[0] + x
                y_idx = start[1] + y

                tmp = grid.get(x_idx, {})
                grid[x_idx] = tmp
                n = tmp.get(y_idx, Node(x_idx, y_idx))
                n.claims.append(claimer)
                grid[x_idx][y_idx] = n


    count = 0
    for x in grid:
        for y in grid[x]:
            n = grid[x][y]
            if len(n.claims) >= 2:
                count += 1
    print "part1():", count

with open("input.txt") as f:
    for line in f:
        line = line.strip().split()
        #print line
        claimer = line[0][1:]
        start = [int(x) for x in line[2][:-1].split(",")]
        size = [int(x) for x in line[3].split("x")]

        ok = True
        for y in range(0, size[1]):
            for x in range(0, size[0]):
                x_idx = start[0] + x
                y_idx = start[1] + y

                n = grid[x_idx][y_idx]
                if len(n.claims) > 1:
                    ok = False
                    break
            if not ok:
                break
        if ok:
            print "part2():", claimer
            break