from sets import Set

def part1():
    with open("input.txt") as f:
        count = 0
        for line in f:
            line = line.strip()
            scale = 1
            if line[0] == "-":
                scale = -1
            count += scale*int(line[1:])
        print "part1():", count

def part2():
    lines = []
    with open("input.txt") as f:
        for line in f:
            scale = 1
            if line[0] == "-":
                scale = -1
            lines.append(scale*int(line[1:]))

    found = False
    count = 0
    visited = Set()
    while not found:
        for line in lines:
            if count in visited:
                found = True
                break
            visited.add(count)
            count += line
    print "part2():", count

part1()
part2()