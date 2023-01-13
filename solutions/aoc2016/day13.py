from register import register_solution

import queue
from time import sleep

favorite_number = 1364
goal = (31, 39)


class Node:
    def __init__(self, x, y, steps):
        self.x = x
        self.y = y
        self.pos = (x, y)
        self.steps = steps

    def __str__(self):
        return "{}:{}:{}".format(self.pos, self.distance(), self.steps)

    def __repr__(self):
        return self.__str__()

    def isGoal(self):
        return self.pos == goal

    def distance(self):
        return abs(goal[0] - self.x) + abs(goal[1] - self.y)


def openWall(x, y):
    num = x*x + 3*x + 2 * x*y + y + y*y + favorite_number
    binary = "{0:b}".format(num)
    one_bits = 0
    for c in binary:
        if c == '1':
            one_bits += 1
    resp = None
    moded = one_bits % 2
    if one_bits % 2 == 0:
        resp = '.'
    else:
        resp = '#'
    return resp


@register_solution(2016, 13, 1)
def part1(filename):
    pQueue = queue.PriorityQueue()
    seen = set()

    start = Node(1, 1, 0)
    seen.add(start.pos)
    pQueue.put((start.distance(), start))

    while not pQueue.empty():
        current = pQueue.get()[1]
        if current.isGoal():
            print("(part1):", current.steps)
            break

        for i in [-1, 1]:
            x1, y1 = current.x + i, current.y
            if x1 >= 0 and y1 >= 0:
                type1 = openWall(x1, y1)
                if type1 != '#' and (x1, y1) not in seen:
                    n1 = Node(x1, y1, current.steps + 1)
                    seen.add(n1.pos)
                    pQueue.put((n1.pos, n1))

            x2, y2 = current.x, current.y + i
            if x2 >= 0 and y2 >= 0:
                type2 = openWall(x2, y2)
                if type2 != '#' and (x2, y2) not in seen:
                    n2 = Node(x2, y2, current.steps + 1)
                    seen.add(n2.pos)
                    pQueue.put((n2.pos, n2))


@register_solution(2016, 13, 2)
def part2(filename):
    pQueue = queue.PriorityQueue()
    seen = set()

    start = Node(1, 1, 0)
    seen.add(start.pos)
    pQueue.put((start.distance(), start))

    while not pQueue.empty():
        current = pQueue.get()[1]
        if current.steps == 50:
            continue

        for i in [-1, 1]:
            x1, y1 = current.x + i, current.y
            if x1 >= 0 and y1 >= 0:
                type1 = openWall(x1, y1)
                if type1 != '#' and (x1, y1) not in seen:
                    n1 = Node(x1, y1, current.steps + 1)
                    seen.add(n1.pos)
                    pQueue.put((n1.pos, n1))

            x2, y2 = current.x, current.y + i
            if x2 >= 0 and y2 >= 0:
                type2 = openWall(x2, y2)
                if type2 != '#' and (x2, y2) not in seen:
                    n2 = Node(x2, y2, current.steps + 1)
                    seen.add(n2.pos)
                    pQueue.put((n2.pos, n2))

    print("(part2):", len(seen))
