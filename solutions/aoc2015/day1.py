from register import register_solution


@register_solution(2015, 1, 1)
def part1(filename):
    with open(filename) as f:
        floor = 0
        for line in f:
            for c in line:
                if c == "(":
                    print
                    "("
                    floor += 1
                elif c == ")":
                    print
                    ")"
                    floor -= 1

        print(floor)


@register_solution(2015, 1, 2)
def part2(filename):
    with open(filename) as f:
        floor = 0
        i = 1
        for line in f:
            for c in line:
                if c == "(":
                    floor += 1
                elif c == ")":
                    floor -= 1
                if floor < 0:
                    print(i)
                    break
                i += 1
