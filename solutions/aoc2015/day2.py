from register import register_solution


@register_solution(2015, 2, 1)
def part1(filename):
    with open(filename) as f:
        area = 0
        for line in f:
            dimensions = [int(x) for x in line.strip().split('x')]
            a = dimensions[0] * dimensions[1]
            b = dimensions[0] * dimensions[2]
            c = dimensions[1] * dimensions[2]
            slack = min([a, b, c])
            subarea = 2 * a + 2 * b + 2 * c + slack
            area += subarea
        print( "Total Area:", area)


@register_solution(2015, 2, 2)
def part2(filename):
    with open(filename) as f:
        length = 0
        for line in f:
            dimensions = sorted([int(x) for x in line.strip().split('x')])
            sublength = 2 * dimensions[0] + 2 * dimensions[1]
            sublength += dimensions[0] * dimensions[1] * dimensions[2]
            print
            sublength
            length += sublength
        print("Total length:", length)
