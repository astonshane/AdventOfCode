from register import register_solution

import re
from copy import deepcopy, copy
from queue import Queue

class Generator:
    def __init__(self, phrase, secondary_init=None):
        if secondary_init is None:
            self.name = phrase.strip().split(' ')[0]
        else:
            self.name = secondary_init

    def __str__(self):
        return "{%s generator}" % self.name

    def __repr__(self):
        return self.__str__()

    def __lt__(self, other):
        x = self.__str__()
        y = other.__str__()
        return x < y

    def __gt__(self, other):
        x = self.__str__()
        y = other.__str__()
        return x > y

    def __eq__(self, other):
        x = self.__str__()
        y = other.__str__()
        return x == y

class Microchip:
    def __init__(self, phrase, secondary_init=None):
        if secondary_init is None:
            self.name = phrase.strip().strip(',').split('-')[0]
        else:
            self.name = secondary_init

    def __str__(self):
        return "{%s microchip}" % self.name

    def __repr__(self):
        return self.__str__()

    def __cmp__(self, other):
        def cmp(a, b):
            return (a > b) - (a < b)
        return cmp(self.__str__(), other.__str__())

    def __lt__(self, other):
        x = self.__str__()
        y = other.__str__()
        return x < y

    def __gt__(self, other):
        x = self.__str__()
        y = other.__str__()
        return x > y

    def __eq__(self, other):
        x = self.__str__()
        y = other.__str__()
        return x == y

class Building:
    def __init__(self):
        self.floors = []
        self.depth = 0

    def finalState(self):
        return (len(self.floors[0]) == 0) and (len(self.floors[1]) == 0) and (len(self.floors[2]) == 0)

    def elevatorFloor(self):
        for i in range(0, len(self.floors)):
            if 'elevator' in self.floors[i]:
                return i
        return -1

    def __str__(self):
        retval = "#####################\n"
        for i in range(len(self.floors)-1, -1, -1):
            retval += "F%d " % (i+1)+ str(self.floors[i])+ "\n"
        retval += "#####################"
        return retval

    def __repr__(self):
        return self.__str__()

    def findPairPos(self):
        pairPos = {}

        for i in range(0, len(self.floors)):
            for element in self.floors[i]:

                if isinstance(element, Generator):
                    if element.name not in pairPos:
                        pairPos[element.name] = [-1, -1]
                    pairPos[element.name][0] = i
                elif isinstance(element, Microchip):
                    if element.name not in pairPos:
                        pairPos[element.name] = [-1, -1]
                    pairPos[element.name][1] = i
        return list(pairPos.values())

    def stringify(self):
        state = ""

        elevatorLevel = self.elevatorFloor()
        state += "E%d;" % elevatorLevel

        pairPos = self.findPairPos()
        pairPos.sort()
        state += str(pairPos)
        return state


building = Building()
states = set()
queue = Queue()

def addToQueue(b):
    # make sure each floor is still valid (ie. nothing will be destroyed)
    for floor in b.floors:
        # split by type
        generators = []
        microchips = []
        for element in floor:
            if isinstance(element, Generator):
                generators.append(element)
            elif isinstance(element, Microchip):
                microchips.append(element)

        # make sure each microchip has its generator OR there are no generator present
        for chip in microchips:
            matching_generator = False
            for gen in generators:
                if chip.name == gen.name:
                    matching_generator = True
            if not matching_generator and len(generators) > 0:
                return False
    # make sure this state hasn't been reached already
    state = b.stringify()
    if state in states:
        return False

    # add it to the queue / states
    states.add(state)
    queue.put(b)
    return True


def parse_input(filename):
    # parse the initial state
    with open(filename) as f:
        for line in f:
            line = line.strip()

            singleRegex = '.* contains a (.*).'
            multiRegex = '.* contains a (.*) and a (.*).'

            m1 = re.search(multiRegex, line)
            m2 = re.search(singleRegex, line)

            floor_contents = []

            if m1 != None:
                things = m1.groups()[0].split(', a')
                for thing in things:
                    if 'generator' in thing:
                        floor_contents.append(Generator(thing))
                    else:
                        floor_contents.append(Microchip(thing))

                if 'generator' in m1.groups()[1]:
                    floor_contents.append(Generator(m1.groups()[1]))
                else:
                    floor_contents.append(Microchip(m1.groups()[1]))

            elif m2 != None:
                if 'generator' in m2.groups()[0]:
                    floor_contents.append(Generator(m2.groups()[0]))
                else:
                    floor_contents.append(Microchip(m2.groups()[0]))

            building.floors.append(floor_contents)
        building.floors[0].append('elevator')

def execute():
    print(building)

    # add the initial state / building to the queue
    states.add(building.stringify())
    queue.put(building)

    while not queue.empty():
        b = queue.get()
        # check if final state...
        if b.finalState():
            print("(answer):", b.depth)
            break

        elevatorLevel = b.elevatorFloor()

        for i in [1, -1]:
            if i == -1:
                empty = True
                for j in range(elevatorLevel - 1, -1, -1):
                    if len(b.floors[j]) != 0:
                        empty = False
                if empty:
                    continue
            # move elevator up!
            if (i == 1 and elevatorLevel != 3) or (i == -1 and elevatorLevel != 0):
                new_base_b = deepcopy(b)
                new_base_b.depth += 1
                new_base_b.floors[elevatorLevel].remove('elevator')
                new_base_b.floors[elevatorLevel + i].append('elevator')

                # move one thing in elevator
                for element in new_base_b.floors[elevatorLevel]:
                    new_b = deepcopy(new_base_b)
                    # print(new_base_b)
                    # print(new_b)
                    # print(element, elevatorLevel, new_b.floors[elevatorLevel])
                    new_b.floors[elevatorLevel].remove(element)
                    new_b.floors[elevatorLevel + i].append(element)
                    addToQueue(new_b)

                    # move two things in elevator
                    for el2 in new_b.floors[elevatorLevel]:
                        new_b2 = deepcopy(new_b)
                        new_b2.floors[elevatorLevel].remove(el2)
                        new_b2.floors[elevatorLevel + i].append(el2)
                        addToQueue(new_b2)


@register_solution(2016, 11, 1)
def part1(filename):
    parse_input(filename)
    execute()


@register_solution(2016, 11, 2)
def part2(filename):
    parse_input(filename)

    building.floors[0].append(Generator('', 'elerium'))
    building.floors[0].append(Microchip('', 'elerium'))
    building.floors[0].append(Generator('', 'dilithium'))
    building.floors[0].append(Microchip('', 'dilithium'))

    execute()
