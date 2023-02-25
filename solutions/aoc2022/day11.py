from register import register_solution
import re
from operator import mul, add

constant = 1

class Monkey:
    def __init__(self, lines):
        global constant

        # line 1: number
        r = re.compile(r'Monkey (\d+):')
        m = r.match(lines[0])
        self.number = int(m.group(1))

        # line 2: starting items
        self.items = [int(x) for x in lines[1].split(':')[1].split(', ')]

        # line 3: operation / op value
        line = lines[2].split('= ')[1].split(' ')

        operator = add if line[1] == '+' else mul
        self.operation = lambda old: operator(
            int(line[0]) if line[0] != 'old' else old,
            int(line[2]) if line[2] != 'old' else old
        )

        # line 4: test
        self.test = int(lines[3].split(' ')[-1])
        constant *= self.test

        # line 5: if true
        self.true_partner = int(lines[4].split(' ')[-1])

        # line 6: if false
        self.false_partner = int(lines[5].split(' ')[-1])

        self.monkeys = None
        self.inspected = 0

    def take_turn(self, p1=True):
        # print("Starting Turn for Monkey: %d" % self.number)
        for item in self.items:
            self.inspected += 1
            worry_level = self.operation(item)
            if p1:
                worry_level = int(worry_level / 3)
            else:
                worry_level = worry_level % constant
            test = worry_level % self.test == 0
            # print(item, worry_level, test)
            self.throw(test, worry_level)
        self.items = []

    def throw(self, test, val):
        #val = val % self.test
        if test:
            # print("sending %d to monkey %d" % (val, self.true_partner))
            self.monkeys[self.true_partner].items.append(val)
        else:
            # print("sending %d to monkey %d" % (val, self.false_partner))
            self.monkeys[self.false_partner].items.append(val)


def parse_input(filename):
    monkeys = []
    with open(filename) as f:
        monkey_lines = [f.readline().strip()]
        for line in f:
            line = line.strip()
            if len(line) > 0:
                monkey_lines.append(line)
            else:
                m = Monkey(monkey_lines)
                monkeys.append(m)
                monkey_lines = []
        monkeys.append(Monkey(monkey_lines))
    for monkey in monkeys:
        monkey.monkeys = monkeys
    return monkeys


@register_solution(2022, 11, 1)
def part1(filename):
    monkeys = parse_input(filename)

    round = 0
    while round < 20:
        round += 1
        # print("Round:", round)
        for monkey in monkeys:
            monkey.take_turn()
        # for monkey in monkeys:
        #     print("Monkey %d:" % monkey.number, monkey.items)

    inspected = [m.inspected for m in monkeys]
    inspected.sort()
    print("Part 1:", inspected[-1]*inspected[-2])


@register_solution(2022, 11, 2)
def part2(filename):
    monkeys = parse_input(filename)

    round = 0
    while round < 10000:
        round += 1
        # if round % 100 == 0:
        #     print("Round:", round)
        for monkey in monkeys:
            monkey.take_turn(False)
        # for monkey in monkeys:
        #     print("Monkey %d:" % monkey.number, monkey.items)

    inspected = [m.inspected for m in monkeys]
    inspected.sort()
    print("Part 2:", inspected[-1] * inspected[-2])
