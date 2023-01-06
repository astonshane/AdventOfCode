from register import register_solution


class Position:
    def __init__(self, name):
        self.name = name
        self.x = 0
        self.y = 0

    def __str__(self):
        return "%s(%d,%d)" % (self.name, self.x, self.y)

    def __repr__(self):
        return self.__str__()

    def to_tuple(self):
        return (self.x, self.y)

    def is_touching(self, other):
        if self.x == other.x and self.y in [other.y, other.y+1, other.y-1]:
            return True
        if self.y == other.y and self.x in [other.x, other.x+1, other.x-1]:
            return True
        if (self.x in [other.x-1, other.x+1]) and (self.y in [other.y-1, other.y+1]):
            return True
        return False

    # used to move head
    def move(self, direction):
        if direction == "U":
            self.y += 1
        if direction == "D":
            self.y -= 1
        if direction == "L":
            self.x -= 1
        if direction == "R":
            self.x += 1

    # used to catch T up to head
    def follow(self, other):
        if self.is_touching(other):
            return

        #print("T no longer touching!")
        #print(self, other)
        if self.x == other.x and self.y == other.y+2:
            self.y -= 1
        elif self.x == other.x and self.y == other.y-2:
            self.y += 1
        elif self.y == other.y and self.x == other.x+2:
            self.x -= 1
        elif self.y == other.y and self.x == other.x-2:
            self.x += 1
        elif self.y < other.y and self.x < other.x:
            self.x += 1
            self.y += 1
        elif self.y < other.y and self.x > other.x:
            self.x -= 1
            self.y += 1
        elif self.y > other.y and self.x < other.x:
            self.x += 1
            self.y -= 1
        elif self.y > other.y and self.x > other.x:
            self.x -= 1
            self.y -= 1
        else:
            print("!!! WHOOPS !!!")

        #print("New Tail Location:", self)


# generically solves for any length rope (>1)
def solver(filename, num_knots):
    with open(filename) as f:
        visited = set()

        knots = []
        for i in range(0, num_knots):
            knots.append(Position(str(i)))

        for line in f:
            line = line.split()
            direction = line[0]
            distance = int(line[1])
            for i in range(0, distance):
                h = knots[0]
                h.move(direction)

                for x in range(1, num_knots):
                    t = knots[x]
                    t.follow(h)
                    h = knots[x]

                visited.add(knots[-1].to_tuple())
        print("Visited %d Locations" % len(visited))


@register_solution(2022, 9, 1)
def part1(filename):
    solver(filename, 2)


@register_solution(2022, 9, 2)
def part2(filename):
    solver(filename, 10)