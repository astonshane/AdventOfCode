from register import register_solution


class Reindeer:
    def __init__(self, name, speed, flyTime, restTime):
        self.name = name
        self.speed = speed
        self.flyTime = flyTime
        self.restTime = restTime

        self.pos = 0
        self.flying = True
        self.time = flyTime

        self.points = 0

    def __str__(self):
        return "%s (%d %d)" % (self.name, self.pos, self.points)

    def __repr__(self):
        return self.__str__()

    def increment(self):
        if self.time == 0:
            if self.flying:
                self.time = self.restTime
            else:
                self.time = self.flyTime
            self.flying = not self.flying
        if self.time > 0:
            self.time -= 1
            if self.flying:
                self.pos += self.speed


@register_solution(2015, 14, 1)
def part1(filename):
    time = 2503
    reindeer = []
    with open(filename) as f:
        for line in f:
            line = line.split(' ')
            reindeer.append(Reindeer(line[0], int(line[3]), int(line[6]), int(line[13])))
    for i in range(0, time):
        for r in reindeer:
            r.increment()
    #reindeer.sort(key=lambda x: x.pos)
    print(max([x.pos for x in reindeer]))

@register_solution(2015, 14, 2)
def part2(filename):
    time = 2503
    reindeer = []
    with open(filename) as f:
        for line in f:
            line = line.split(' ')
            reindeer.append(Reindeer(line[0], int(line[3]), int(line[6]), int(line[13])))
    for i in range(0, time):
        for r in reindeer:
            r.increment()
        reindeer.sort(key=lambda x: x.pos)
        max_pos = reindeer[-1].pos
        for r in reindeer:
            if r.pos == max_pos:
                r.points += 1

    print(max([x.points for x in reindeer]))
