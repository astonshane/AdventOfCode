import sys


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

# ######################
if len(sys.argv) != 3:
    print "need an input file and time step"
    exit(1)

time = int(sys.argv[2])
reindeer = []

f = open(sys.argv[1])
for line in f:
    line = line.split(' ')
    reindeer.append(Reindeer(line[0], int(line[3]), int(line[6]), int(line[13])))

print reindeer
for i in range(0, time):
    for r in reindeer:
        r.increment()
    reindeer.sort(key=lambda x: x.pos)
    max_pos = reindeer[-1].pos
    for r in reindeer:
        if r.pos == max_pos:
            r.points += 1

    reindeer.sort(key=lambda x: x.points)
    print reindeer
