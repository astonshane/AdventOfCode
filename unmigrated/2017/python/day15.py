A_FACTOR = 16807
B_FACTOR = 48271

A_MULTIPLE = 4
B_MULTIPLE = 8

DIVISOR = 2147483647

class Generator:
    def __init__(self, a, base, part2=False):
        self.val = base
        self.factor = A_FACTOR if a else B_FACTOR
        self.multiple = A_MULTIPLE if a else B_MULTIPLE
        self.part2 = part2

    def _next(self):
        self.val = (self.val * self.factor) % DIVISOR

    def _part2(self):
        self._next()
        while self.val % self.multiple:
            self._next()

    def next(self):
        return self._part2() if self.part2 else self._next()

def part1():
    ROUNDS = 40000000

    with open("inputs/day15.txt") as f:
        a = Generator(True, int(f.readline().strip().split()[-1]))
        b = Generator(False, int(f.readline().strip().split()[-1]))
        count = 0

        for i in range(0, ROUNDS):
            a.next()
            b.next()
            if i % 1000000 == 0:
                print(i)

            # gives the lowest 16 bits
            if a.val & 0xFFFF == b.val & 0xFFFF:
                count += 1

        print("part1:", count)

def part2():
    ROUNDS = 5000000

    with open("inputs/day15.txt") as f:
        a = Generator(True, int(f.readline().strip().split()[-1]), True)
        b = Generator(False, int(f.readline().strip().split()[-1]), True)
        count = 0

        for i in range(0, ROUNDS):
            a.next()
            b.next()
            if i % 1000000 == 0:
                print(i)

            # gives the lowest 16 bits
            if a.val & 0xFFFF == b.val & 0xFFFF:
                #print(i, a.val, b.val)
                count += 1

        print("part2:", count)

#part1()
part2()
