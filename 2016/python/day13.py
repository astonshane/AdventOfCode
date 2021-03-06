import Queue
from sets import Set
from time import sleep
from colorama import init, Fore, Back

init(autoreset=True)

favorite_number = 1364
goal = (31, 39)

class Node:
    def __init__(self, x, y, steps):
        self.x = x
        self.y = y
        self.pos = (x, y)
        self.steps = steps

    def __str__(self):
        return "{}:{}:{}".format(self.pos, self.distance(), self.steps)

    def __repr__(self):
        return self.__str__()

    def isGoal(self):
        return self.pos == goal

    def distance(self):
        return abs(goal[0] - self.x) + abs(goal[1] - self.y)


def openWall(x, y):
    #print "pos", x, y
    num = x*x + 3*x + 2 * x*y + y + y*y + favorite_number
    #print "num", num
    binary = "{0:b}".format(num)
    #print "binary", binary
    one_bits = 0
    for c in binary:
        if c == '1':
            one_bits += 1
    #print "one_bits", one_bits
    resp = None
    moded = one_bits % 2
    #print "moded", moded
    if one_bits % 2 == 0:
        resp = '.'
    else:
        resp = '#'
    #print x, y, resp
    return resp

def part1(viz=False):
    if viz:
        print '\033[2J' # clear the screen

        # start by drawing the maze out
        for i in range(0, 50):
            for j in range(0, 60):
                cursor_pos = '\033[%d;%dH' % (5+i, 20+j)
                color = ''
                kind = ''
                if (j, i) == goal:
                    color = Back.YELLOW
                    kind = '0'
                else:
                    kind = openWall(j, i)
                    color = ''
                    if kind == '#':
                        color = Fore.RED # red
                    else:
                        color = Fore.BLUE # blue
                print cursor_pos+color+kind
    raw_input()
    pQueue = Queue.PriorityQueue()
    seen = Set()

    start = Node(1, 1, 0)
    seen.add(start.pos)
    pQueue.put((start.distance(), start))

    while not pQueue.empty():
        current = pQueue.get()[1]
        if current.isGoal():
            print "(part1):", current.steps
            break
        if viz:
            cursor_pos = '\033[%d;%dH' % (5+current.y, 20+current.x)
            sleep(0.03) # slow it down so we can see it!
            print cursor_pos + '0'

        for i in [-1, 1]:
            x1, y1 = current.x+i, current.y
            if x1 >= 0 and y1 >= 0:
                type1 = openWall(x1, y1)
                if type1 != '#' and (x1, y1) not in seen:
                    n1 = Node(x1, y1, current.steps+1)
                    seen.add(n1.pos)
                    pQueue.put((n1.pos, n1))

            x2, y2 = current.x, current.y+i
            if x2 >= 0 and y2 >= 0:
                type2 = openWall(x2, y2)
                if type2 != '#' and (x2, y2) not in seen:
                    n2 = Node(x2, y2, current.steps+1)
                    seen.add(n2.pos)
                    pQueue.put((n2.pos, n2))
    if viz:
        raw_input("enter to continue")
        print '\033[2J' # clear the screen

def part2(viz=False):
    if viz:
        print '\033[2J' # clear the screen

        # start by drawing the maze out
        for i in range(0, 50):
            for j in range(0, 60):
                cursor_pos = '\033[%d;%dH' % (5+i, 20+j)
                kind = openWall(j, i)
                color = ''
                if kind == '#':
                    color = Fore.RED # red
                else:
                    color = Fore.BLUE # blue
                print cursor_pos+color+kind

    pQueue = Queue.PriorityQueue()
    seen = Set()

    start = Node(1, 1, 0)
    seen.add(start.pos)
    pQueue.put((start.distance(), start))

    while not pQueue.empty():
        current = pQueue.get()[1]
        if viz:
            cursor_pos = '\033[%d;%dH' % (5+current.y, 20+current.x)
            sleep(0.03) # slow it down so we can see it!
            print cursor_pos + '0'
        if current.steps == 50:
            continue

        for i in [-1, 1]:
            x1, y1 = current.x+i, current.y
            if x1 >= 0 and y1 >= 0:
                type1 = openWall(x1, y1)
                if type1 != '#' and (x1, y1) not in seen:
                    n1 = Node(x1, y1, current.steps+1)
                    seen.add(n1.pos)
                    pQueue.put((n1.pos, n1))

            x2, y2 = current.x, current.y+i
            if x2 >= 0 and y2 >= 0:
                type2 = openWall(x2, y2)
                if type2 != '#' and (x2, y2) not in seen:
                    n2 = Node(x2, y2, current.steps+1)
                    seen.add(n2.pos)
                    pQueue.put((n2.pos, n2))

    print "(part2):", len(seen)

    if viz:
        raw_input("enter to exit")
        print '\033[2J' # clear the screen


part1(viz=True)
part2(viz=True)
