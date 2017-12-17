import math
import sys

input = 361527

def printTable(table):
    print "### start ###"
    for row in table:
        print row
    print "### end ###"

def move(x, y, dir):
    if dir == "R":
        x += 1
    elif dir == "U":
        y -= 1
    elif dir == "L":
        x -= 1
    elif dir == "D":
        y += 1
    return x, y

def part1():
    table = []
    for i in range(0, 1000):
        row = [0 for x in range(0,1000)]
        table.append(row)

    x = y = 3
    table[y][x] = 1

    dirs = "RULD"
    size = 1
    count = 2

    while (True):
        for i in range(0,2):
            for dir in [dirs[i*2], dirs[i*2+1]]:
                for k in range(0, size):
                    x, y = move(x, y, dir)
                    table[y][x] = count

                    if count == input:
                        print "Part1:", abs(x) + abs(y)
                        return


                    count += 1
                    #printTable(table)
            size += 1


def calculate(table, x, y):
    sum = 0

    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue
            nx = x+i
            ny = y+j
            #print nx, ny, table[ny][nx]
            sum += table[ny][nx]
    #print sum
    return sum

def part2():
    table = []
    for i in range(0, 15):
        row = [0 for x in range(0,15)]
        table.append(row)

    x = y = 3
    table[y][x] = 1

    dirs = "RULD"
    size = 1

    while (True):
        for i in range(0,2):
            for dir in [dirs[i*2], dirs[i*2+1]]:
                for k in range(0, size):
                    x, y = move(x, y, dir)
                    calc = calculate(table, x, y)
                    table[y][x] = calc
                    if calc > input:
                        print "Part2:", calc
                        return
                    #printTable(table)

            size += 1

part1()
part2()
