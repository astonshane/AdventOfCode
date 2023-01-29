from register import register_solution
import re
import plotext as plt

class Point:
    def __init__(self, x, y, xvel, yvel):
        self.x = x
        self.y = y

        self.xx = xvel
        self.yy = yvel

    def step(self):
        self.x += self.xx
        self.y += self.yy


def parse_input(filename):
    all_points = []
    matcher = re.compile(r'position=<(.*),(.*)> velocity=<(.*),(.*)>')
    with open(filename) as f:
        for line in f:
            match = matcher.match(line)
            [x, y, xvel, yvel] = [int(m.strip()) for m in match.groups()]
            p = Point(x, y*-1, xvel, yvel*-1)
            all_points.append(p)
    return all_points


def print_points(all_points):
    all_x = [p.x for p in all_points]
    all_y = [p.y for p in all_points]

    min_x = min(all_x)
    max_x = max(all_x)
    min_y = min(all_y)
    max_y = max(all_y)

    x_diff = max_x - min_x
    y_diff = max_y - min_y

    count = 0

    while y_diff > 10:
        for point in all_points:
            point.step()
        count += 1
        all_x = [p.x for p in all_points]
        all_y = [p.y for p in all_points]

        min_x = min(all_x)
        max_x = max(all_x)
        min_y = min(all_y)
        max_y = max(all_y)

        x_diff = max_x - min_x
        y_diff = max_y - min_y

    #print(all_x, min_x, max_x)
    #print(all_y, min_y, max_y)

    # for point in all_points:
    #     print(point.x, point.y)
    # print(len(all_points))

    while True:
        plt.scatter(all_x, all_y)
        plt.xfrequency(1)
        plt.yfrequency(1)
        plt.plotsize(250,50)
        plt.show()
        print("Seconds:", count)
        input('press any key to continue...')
        plt.clear_data()
        for point in all_points:
            point.step()
        all_x = [p.x for p in all_points]
        all_y = [p.y for p in all_points]

    # fig.show()


@register_solution(2018, 10, 1)
def part1(filename):
    all_points = parse_input(filename)
    print_points(all_points)


@register_solution(2018, 10, 2)
def part2(filename):
    pass
