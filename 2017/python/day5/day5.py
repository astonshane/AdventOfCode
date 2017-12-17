import sys
from sets import Set
import copy

def printTape(tape, index):
    #tape[index] = 'x'
    print tape, index

def part1():
    filename = sys.argv[1]
    with open(filename) as input:

        tape = [int(line) for line in input]

        index = 0
        steps = 0

        while(index > -1 and index < len(tape)):
            #printTape(copy.copy(tape), index)
            steps += 1

            move = tape[index]
            tape[index] += 1
            index += move


        print "Part1:", steps
part1()

def part2():
    filename = sys.argv[1]
    with open(filename) as input:

        tape = [int(line) for line in input]

        index = 0
        steps = 0

        while(index > -1 and index < len(tape)):
            #printTape(copy.copy(tape), index)
            steps += 1

            move = tape[index]

            if tape[index] >= 3:
                tape[index] -= 1
            else:
                tape[index] += 1

            index += move


        print "Part2:", steps
part2()
