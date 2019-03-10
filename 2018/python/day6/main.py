from pprint import pprint
import copy

class Point:
    def __init__(self, x, y, name=None):
        self.x = x
        self.y = y
        self.name = name

    def __cmp__(self, other):
        return cmp(self.name, other.name)

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.__str__()

    def __hash__(self):
        return hash(self.name)

def manhattan(p1, p2):
    return abs(p1.x-p2.x) + abs(p1.y - p2.y)

def calcPoints(points, low, high):
    for x in range(low, high):
        for y in range(low, high):
            p1 = Point(x, y)

            min_dist = None
            min_point = None

            for p2 in points.keys():
                man = manhattan(p1, p2)
                if min_dist is None or man < min_dist:
                    min_dist = man
                    min_point = p2
            
            if min_dist != 0:
                points[min_point] += 1
    return points

def part1():
    with open("input.txt") as f:
        points = {}

        name = ord('A')
        for line in f:
            [x, y] = [int(x) for x in line.strip().split(", ")]
            point = Point(x, y, chr(name))
            points[point] = 1
            name += 1
        
        #pprint(points, width=1)
        #print "####################"

        low = -500
        high = 500
        points1 = calcPoints(copy.deepcopy(points), -300, 500)
        pprint(points1, width=1)
        points2 = calcPoints(copy.deepcopy(points), -400, 800)
        pprint(points2, width=1)


        non_infinite = []
        for p in points1:
            p1 = points1[p]
            p2 = points2[p]
            print p, p1, p2, abs(p1 - p2)
            if (p1-p2) == 0:
                non_infinite.append(p1)
        print max(non_infinite)

def part2():
    with open("input.txt") as f:
        points = []

        name = ord('A')
        for line in f:
            [x, y] = [int(x) for x in line.strip().split(", ")]
            point = Point(x, y, chr(name))
            points.append(point)
            name += 1
        
        low = 0
        high = 2000
        max_allowed = 10000

        in_range = 0

        for x in range(low, high):
            for y in range(low, high):
                p = Point(x, y, "(%d,%d)" % (x, y))
                #print p,
                total = 0
                for p2 in points:
                    total += manhattan(p, p2)
                #print total
                if total < max_allowed:
                    in_range += 1
        print in_range

        

# part1()
part2()