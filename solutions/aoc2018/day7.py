from register import register_solution
import re


def letter_cost(letter, modifier=60):
    return modifier + (ord(letter) - ord('A') + 1)


class Rules:
    def __init__(self, filename):
        rules = {}
        matcher = re.compile(r'Step (.) must be finished before step (.) can begin\.')
        with open(filename) as f:
            for line in f:
                line = line.strip()
                (x, y) = matcher.match(line).groups()
                if x not in rules:
                    rules[x] = set()
                if y not in rules:
                    rules[y] = set()
                rules[y].add(x)
        self.rules = rules

    def ready(self):
        empties = []
        for key in self.rules:
            if len(self.rules[key]) == 0:
                empties.append(key)

        empties.sort()
        return empties

    def pop(self, letter):
        # print("popping: ", letter)
        self.rules.pop(letter)

    def finish(self, finished):
        # print("finishing:", finished)
        for key in self.rules:
            if finished in self.rules[key]:
                self.rules[key].remove(finished)

    def __len__(self):
        return len(self.rules)


class Worker:
    def __init__(self):
        self.letter = None
        self.duration_remaining = 0

    def take(self, letter):
        if letter is None:
            return
        # print("taking:", letter)
        self.letter = letter
        self.duration_remaining = letter_cost(letter, 60)

    def step(self):
        if self.letter is None:
            return
        self.duration_remaining -= 1
        # print(self.letter, self.duration_remaining)
        if self.duration_remaining == 0:
            l = self.letter
            self.letter = None
            self.duration_remaining = 0
            return l


@register_solution(2018, 7, 1)
def part1(filename):
    rules = Rules(filename)
    order = ""
    while len(rules) > 0:
        ready_letters = rules.ready()
        x = ready_letters[0]
        rules.pop(x)
        rules.finish(x)
        order += x

    print("Part1:", order)


@register_solution(2018, 7, 2)
def part2(filename):
    rules = Rules(filename)
    workers = [Worker() for _ in range(0, 5)]
    duration = 0

    while len(rules) > 0:
        # print("duration", duration)
        ready_letters = rules.ready()
        # print("ready letters", ready_letters)
        for worker in workers:
            if worker.letter is None and len(ready_letters) > 0:
                x = ready_letters[0]
                ready_letters = ready_letters[1:]
                # print("new ready letters", ready_letters)
                rules.pop(x)
                worker.take(x)

            l = worker.step()
            if l is not None:
                rules.finish(l)
        duration += 1
    duration += max([w.duration_remaining for w in workers])
    print("Part2:", duration)

