import re

class Particle:
    name = -1
    pos = None
    vel = None
    acc = None
    
    def __init__(self, i, line):
        self.name = i

        match = re.match("p=<([-\d]+),([-\d]+),([-\d]+)>, v=<([-\d]+),([-\d]+),([-\d]+)>, a=<([-\d]+),([-\d]+),([-\d]+)>", line)
        nums = [int(x) for x in match.groups()]

        self.pos = nums[0:3]
        self.vel = nums[3:6]
        self.acc = nums[6:]

    def __str__(self):
        return f"({self.name} pos: {self.pos} vel: {self.vel} acc: {self.acc})"

    def __repr__(self):
        return self.__str__()

    # executes 1 tick and returns manhattan distance from 0,0,0
    def tick(self):
        for i in range(0, 3):
            self.vel[i] += self.acc[i]
            self.pos[i] += self.vel[i]
        return sum([abs(x) for x in self.pos])



with open('inputs/day20.txt') as f:
    particles = []
    i = 0
    for line in f:
        particles.append(Particle(i, line))

    print(particles)

    part1 = False

    for i in range(0, 1000):
        distances = [x.tick() for x in particles]

        if part1:
            closest_val = min(distances)
            closest = distances.index(closest_val)
            if i % 100 == 0:
                print(f"closest after step {i}: {closest}")
        else:
            collided = []
            uncollided = []
            if i % 100 == 0:
                print(f"particle count: {len(particles)}")
            for p in particles:
                if p.pos in collided:
                    continue
                if p.pos in [x.pos for x in uncollided]:
                    collided.append(p.pos)
                    uncollided = [x for x in uncollided if x.pos != p.pos]       
                else:
                    uncollided.append(p)

            particles = uncollided
                
    
    if part1:
        print(closest)