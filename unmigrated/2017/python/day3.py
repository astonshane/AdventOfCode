import math
import sys
from enum import Enum

input = 361527

def printTable(table):
    print("### start ###")
    for row in table:
        print(row)
    print("### end ###")

class Direction(Enum):
    RIGHT=0
    UP=1
    LEFT=2
    DOWN=3

    # return the next direction to move in order of the spiral
    def next(self):
        new_val = (self.value + 1) % 4
        return Direction(new_val)

    def isOdd(self):
        return self.value % 2 != 0

    # given a (x,y) coord, return the next one assuming we move in the current direction
    def move(self, x, y):
        if self is Direction.RIGHT:
            x += 1
        elif self is Direction.UP:
            y -= 1
        elif self is Direction.LEFT:
            x -= 1
        elif self is Direction.DOWN:
            y += 1            
        return x, y

def part1():
    # pre-populate the matrix (this sucks)
    table = []
    for i in range(0, 400):
        row = [0 for x in range(0,400)]
        table.append(row)

    x = y = 3
    table[y][x] = 1

    size = 1
    count = 2
    current_direction = Direction.DOWN

    while (True):
        current_direction = current_direction.next()
        
        for k in range(0, size):
            x,y = current_direction.move(x,y)
            table[y][x] = count

            if count == input:
                print("Part1:", abs(x) + abs(y))
                return


            count += 1
            #printTable(table)
        if current_direction.isOdd():
            size += 1


def calculate(table, x, y):
    sum = 0

    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue
            nx = x+i
            ny = y+j
            sum += table[ny][nx]
    return sum

def part2():
    table = []
    for i in range(0, 15):
        row = [0 for x in range(0,15)]
        table.append(row)

    x = y = 3
    table[y][x] = 1

    current_direction = Direction.DOWN
    size = 1

    while (True):
        current_direction = current_direction.next()
        
        for k in range(0, size):
            x,y = current_direction.move(x,y)
            calc = calculate(table, x, y)
            table[y][x] = calc
            if calc > input:
                print("Part2:", calc)
                return
        if current_direction.isOdd():
            size += 1

part1()
part2()