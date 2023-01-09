from register import register_solution
import re

value_regex = 'value (\d+) goes to bot (\d+)'
highlow_regex = 'bot (\d+) gives low to (bot|output) (\d+) and high to (bot|output) (\d+)'

class Bot:
    def __init__(self, num):
        self.num = num
        self.instruction = None
        self.values = []

    def getValues(self):
        return self.values[0], self.values[1]

    def addValue(self, val):
        self.values.append(val)
        self.values.sort()

    def addInstruction(self, inst):
        assert self.instruction is None
        self.instruction = inst

    def __str__(self):
        return "%s" % (self.values)

    def __repr__(self):
        return self.__str__()


class Bin:
    def __init__(self, num):
        self.num = num
        self.values = []

    def addValue(self, val):
        self.values.append(int(val))
        self.values.sort()

    def __str__(self):
        return "%s" % (self.values)

    def __repr__(self):
        return self.__str__()


def parse_input(filename):
    bots = {}
    output_bins = {}

    with open(filename) as f:
        for line in f:

            m = re.search(value_regex, line.strip())
            if m != None:
                value, bot = int(m.groups()[0]), int(m.groups()[1])
                if bot not in bots:
                    bots[bot] = Bot(bot)
                bots[bot].addValue(value)
            else:
                m = re.search(highlow_regex, line.strip())
                if m != None:
                    # parse line
                    [source_num, low_type, low_num, high_type, high_num] = m.groups()
                    source_num = int(source_num)
                    low_num = int(low_num)
                    high_num = int(high_num)

                    # init bots if necessary...
                    if int(source_num) not in bots:
                        bots[source_num] = Bot(source_num)

                    if (low_type == "bot") and (low_num not in bots):
                        bots[low_num] = Bot(low_num)
                    elif low_num not in output_bins:
                        output_bins[low_num] = Bin(low_num)

                    if (high_type == "bot") and (high_num not in bots):
                        bots[high_num] = Bot(high_num)
                    elif high_num not in output_bins:
                        output_bins[high_num] = Bin(high_num)

                    # add instruction
                    bots[source_num].addInstruction(line)
    return bots, output_bins


@register_solution(2016, 10, 1)
@register_solution(2016, 10, 2)
def part1(filename):
    bots, output_bins = parse_input(filename)

    instructionsLeft = True
    while (instructionsLeft):
        instructionsLeft = False
        for num in bots:
            if len(bots[num].values) == 2 and bots[num].instruction is not None:
                instructionsLeft = True
                m = re.search(highlow_regex, bots[num].instruction.strip())
                if m != None:
                    # parse line
                    [source_num, low_type, low_num, high_type, high_num] = m.groups()
                    source_num = int(source_num)
                    low_num = int(low_num)
                    high_num = int(high_num)

                    low, high = bots[num].getValues()

                    if [low, high] == [17, 61]:
                        print("(part1):", num)

                    if low_type == "bot":
                        bots[low_num].addValue(low)
                    else:
                        output_bins[low_num].addValue(low)

                    if high_type == "bot":
                        bots[high_num].addValue(high)
                    else:
                        output_bins[high_num].addValue(high)

                    bots[num].values = []

    print("(part2):", output_bins[0].values[0] * output_bins[1].values[0] * output_bins[2].values[0])

