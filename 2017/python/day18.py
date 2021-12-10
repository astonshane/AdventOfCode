import queue

def part1():
    class Computer:
        def __init__(self):
            self.registers = {}
            self.last_played = None
            self.index = 0

        def print(self):
            print(self.index, self.registers)

        def getIndex(self):
            return self.index

        def value(self, x):
            try:
                return int(x)
            except:
                return self.registers.get(x, 0)

        # plays a sound with a frequency equal to the value of X.
        def snd(self, x):
            #print("playing", self.value(x))
            self.last_played = self.value(x)
            self.index += 1

        # sets register X to the value of Y
        def set(self, x, y):
            self.registers[x] = self.value(y)
            self.index += 1

        # increases register X by the value of Y
        def add(self, x, y):
            self.registers[x] = self.value(x) + self.value(y)
            self.index += 1

        # sets register X to the result of multiplying the value contained in register X by the value of Y.
        def mul(self, x, y):
            self.registers[x] = self.value(x) * self.value(y)
            self.index += 1

        # sets register X to the remainder of dividing the value contained in register X by the value of Y (that is, it sets X to the result of X modulo Y)
        def mod(self, x, y):
            self.registers[x] = self.value(x) % self.value(y)
            self.index += 1

        # recovers the frequency of the last sound played, but only when the value of X is not zero. (If it is zero, the command does nothing.)
        def rcv(self, x):
            val = self.value(x)
            if val != 0:
                print("part1:", self.last_played)
                return 1
            self.index += 1

        # jumps with an offset of the value of Y, but only if the value of X is greater than zero. (An offset of 2 skips the next instruction, an offset of -1 jumps to the previous instruction, and so on.)
        def jgz(self, x, y):
            xval = self.value(x)
            if xval > 0:
                self.index += self.value(y)
            else:
                self.index += 1




    computer = Computer()
    cmd_map = {
        "snd": computer.snd,
        "set": computer.set,
        "add": computer.add,
        "mul": computer.mul,
        "mod": computer.mod,
        "rcv": computer.rcv,
        "jgz": computer.jgz
    }
    commands = []

    with open("inputs/day18.txt") as f:
        for line in f:
            line = line.strip().split()
            cmd = line[0]
            args = line[1:]
            commands.append((cmd_map[cmd], args))

    #computer.print()
    index = computer.getIndex()
    while index >= 0 and index < len(commands):
        index = computer.getIndex()
        (cmd, args) = commands[index]
        r = cmd(*args)
        #computer.print()
        if r is not None:
            break

part1()

def part2():
    class Computer:
        def __init__(self, filename, id, sendQ, recvQ):
            self.id = id
            self.registers = {'p': id}
            self.last_played = None
            self.index = 0
            self.sendQ = sendQ
            self.recvQ = recvQ
            self.deadlock = False
            self.send_count = 0
            self.parseFile(filename)
            

        def parseFile(self, filename):
            cmd_map = {
                "snd": self.snd,
                "set": self.set,
                "add": self.add,
                "mul": self.mul,
                "mod": self.mod,
                "rcv": self.rcv,
                "jgz": self.jgz
            }
            self.commands = []

            with open(filename) as f:
                for line in f:
                    line = line.strip().split()
                    cmd = line[0]
                    args = line[1:]
                    self.commands.append((cmd_map[cmd], args))

        def process(self):
            self.deadlock = True
            while self.index >= 0 and self.index < len(self.commands):
                (cmd, args) = self.commands[self.index]
                r = cmd(*args)
                if r == 1: # deadlocked
                    break
                else:
                    self.deadlock = False

        def print(self):
            print("id: %d, index: %d" % (self.id, self.index), self.registers)

        def getIndex(self):
            return self.index

        def value(self, x):
            try:
                return int(x)
            except:
                return self.registers.get(x, 0)

        # sends the value of X to the other program.
        def snd(self, x):
            val = self.value(x)
            #print("id %d sending %d" % (self.id, val))
            self.sendQ.put(val)
            self.index += 1
            self.send_count += 1

        # sets register X to the value of Y
        def set(self, x, y):
            #print("id %d set" % self.id)
            self.registers[x] = self.value(y)
            self.index += 1

        # increases register X by the value of Y
        def add(self, x, y):
            #print("id %d add" % self.id)
            self.registers[x] = self.value(x) + self.value(y)
            self.index += 1

        # sets register X to the result of multiplying the value contained in register X by the value of Y.
        def mul(self, x, y):
            #print("id %d mul" % self.id)
            self.registers[x] = self.value(x) * self.value(y)
            self.index += 1

        # sets register X to the remainder of dividing the value contained in register X by the value of Y (that is, it sets X to the result of X modulo Y)
        def mod(self, x, y):
            #print("id %d mod" % self.id)
            self.registers[x] = self.value(x) % self.value(y)
            self.index += 1

        # receives the next value and stores it in register X
        def rcv(self, x):
            #print("id %d recv" % self.id)
            try:
                val = self.recvQ.get(block=False)
                self.registers[x] = val
                self.index += 1
            except queue.Empty:
                return 1

        # jumps with an offset of the value of Y, but only if the value of X is greater than zero. (An offset of 2 skips the next instruction, an offset of -1 jumps to the previous instruction, and so on.)
        def jgz(self, x, y):
            #print("id %d jgz" % self.id)
            xval = self.value(x)
            if xval > 0:
                self.index += self.value(y)
            else:
                self.index += 1

    q0 = queue.Queue()
    q1 = queue.Queue()

    filename = "inputs/day18.txt"
    p0 = Computer(filename, 0, q1, q0)
    p1 = Computer(filename, 1, q0, q1)

    while not p0.deadlock or not p1.deadlock:
        #print("New Round:")
        #p0.print()
        #p1.print()

        p0.process()
        p1.process()

    print("part2:", p1.send_count)


part2()