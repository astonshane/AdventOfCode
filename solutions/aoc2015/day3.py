from register import register_solution


@register_solution(2015, 3, 1)
def part1(filename):
    with open(filename) as f:
        pos = (0, 0)
        count = set()
        for line in f:
            for c in line.strip():
                count.add(pos)
                if c == '>':
                    pos = (pos[0] + 1, pos[1])
                elif c == "<":
                    pos = (pos[0] - 1, pos[1])
                elif c == "^":
                    pos = (pos[0], pos[1] + 1)
                elif c == "v":
                    pos = (pos[0], pos[1] - 1)

        count.add(pos)
        print(len(count))


@register_solution(2015, 3, 2)
def part2(filename):
    with open(filename) as f:
        # set initial positions
        santa = (0, 0)
        robo = (0, 0)

        visited = set()
        # add initial positon to visited set
        visited.add(santa)

        # 0 == Santa; 1 == Robo Santa
        turn = 0

        for line in f:
            for c in line.strip():
                pos = (0, 0)
                # determine who's turn it is this time
                if turn:
                    pos = robo
                else:
                    pos = santa

                # add the current position to the visited list
                visited.add(pos)

                # move the current actor
                if c == '>':
                    pos = (pos[0] + 1, pos[1])
                elif c == "<":
                    pos = (pos[0] - 1, pos[1])
                elif c == "^":
                    pos = (pos[0], pos[1] + 1)
                elif c == "v":
                    pos = (pos[0], pos[1] - 1)

                # set the new position & change who's turn it is
                if turn:
                    robo = pos
                    turn = 0
                else:
                    turn = 1
                    santa = pos

        visited.add(santa)
        visited.add(robo)
        print(len(visited))