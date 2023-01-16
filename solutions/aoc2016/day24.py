from register import register_solution
from itertools import permutations
import heapq


class Node:
    def __init__(self, name):
        self.name = name
        self.neighbors = []
        self.distance = None

    def reset(self):
        self.distance = None

    def add_neighbor(self, neighbor):
        if neighbor.name != '#':
            self.neighbors.append(neighbor)

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.__str__()

    def __lt__(self, other):
        return self.name < other.name


class Grid:
    def __init__(self, filename):
        self.numbers = []

        self.vertices = []
        self.locations = {}
        self.distances = {}

        grid = []
        with open(filename) as f:
            for line in f:
                line = line.strip()

                numbers = [x for x in line if x not in ['.', '#', '0']]
                self.numbers.extend(numbers)

                line = [Node(x) for x in line]
                # print(line)
                grid.append(line)

        self.numbers.sort()

        for y in range(0, len(grid)):
            for x in range(0, len(grid[y])):
                n = grid[y][x]
                if n.name == '#':
                    continue
                if n.name != '.':
                    self.locations[n.name] = n
                for (xmod, ymod) in [(0,1), (0,-1), (1, 0), (-1, 0)]:
                    xx = x + xmod
                    yy = y + ymod
                    if xx in range(0, len(grid[y])) and yy in range(0, len(grid)):
                        neighbor = grid[yy][xx]
                        n.add_neighbor(neighbor)
                self.vertices.append(n)

    def find_shortest_route(self, part_2):
        shortest_dist = None
        shortest_path = None

        perms = permutations(self.numbers)
        for p in perms:
            perm = ['0']
            if part_2:
                perm.append('0')
            perm[1:1] = list(p)

            dist = 0
            for i in range(0, len(perm)-1):
                start = perm[i]
                end = perm[i+1]
                d = self.shortest_distance(start, end)
                dist += d
            if shortest_dist is None or dist < shortest_dist:
                shortest_dist = dist
                shortest_path = perm
        print(shortest_path, shortest_dist)
        return shortest_dist

    def shortest_distance(self, start, end):
        key = (start, end)
        key2 = (end, start)
        if key in self.distances:
            return self.distances[key]
        if key2 in self.distances:
            return self.distances[key2]

        d = self.dijkstra(start, end)
        self.distances[key] = d
        self.distances[key2] = d
        print("calculated %s <-> %s as %d" % (start, end, d))

        return d

    def dijkstra(self, start, end):
        # make sure all vertices have distance == inf (None)
        for v in self.vertices:
            v.reset()

        s = self.locations[start]
        s.distance = 0
        q = [(0, s)]

        while len(q) > 0:
            (_, n) = heapq.heappop(q)
            if n.name == end:
                return n.distance
            for v in n.neighbors:
                alt = n.distance + 1
                if v.distance is None or alt < v.distance:
                    v.distance = alt
                    heapq.heappush(q, (alt, v))


@register_solution(2016, 24, 1)
def part1(filename):
    grid = Grid(filename)
    grid.find_shortest_route(False)


@register_solution(2016, 24, 2)
def part2(filename):
    grid = Grid(filename)
    grid.find_shortest_route(True)
