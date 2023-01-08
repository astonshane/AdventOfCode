from collections import deque

STEPS = 345

def part1():
    buffer = [0]

    i = 0
    for val in range(1, 2018):
        i = (i + STEPS) % len(buffer) + 1
        buffer.insert(i, val)

    assert(len(buffer) == 2018)
    print("part1:", buffer[(i+1) % 2018])


# some deque magic here to optimize. O(n) inserts for default lists are the killer in part1
def part2():
    buffer = deque()
    buffer.insert(0,0)

    for val in range(1, 50000001):
        buffer.rotate(-STEPS)
        buffer.append(val)

    i = (buffer.index(0) + 1) % 50000000
    print("part2:", buffer[i])

part1()
part2()