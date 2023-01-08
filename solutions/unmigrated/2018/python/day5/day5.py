from sets import Set

def isDestructive(a, b):
    if a.isupper():
        return a.lower() == b
    return a.upper() == b

def reduce(line):
    while True:
        before = len(line)
        
        characters = Set(line.lower())
        for c in characters:
            toReplace1 = "%s%s" % (c, c.upper())
            toReplace2 = "%s%s" % (c.upper(), c)
            line = line.replace(toReplace1, "")
            line = line.replace(toReplace2, "")

        if len(line) == before:
            break
    return len(line)

def part1():
    with open("input.txt") as f:
        line = f.readline().strip()

        units = reduce(line)

        print "Part1: %d units" % units


def part2():
    with open("input.txt") as f:
        line = f.readline().strip()
        characters = Set(line.lower())
        min_units = None
        for c in characters:
            newLine = line.replace(c, "").replace(c.upper(), "")
            units = reduce(newLine)
            if min_units is None or units < min_units:
                min_units = units
        
        print "Part2: %d units" % min_units

        

part1()
part2()