def listReplace(lst, val, rep, m):
    new_list = []
    replaced = 0
    for i in range(0, len(lst)):
        if lst[i] == val and replaced < m:
            replaced += 1
            continue
        new_list.append(lst[i])
    return new_list

def reduce(directions):
    reduced = True

    rules = [
        ("n", "s", ""),
        ("ne", "sw", ""),
        ("nw", "se", ""),
        ("ne", "s", "se"),
        ("se", "n", "ne"),
        ("nw", "s", "sw"),
        ("sw", "n", "nw"),
        ("se", "sw", "s"),
        ("ne", "nw", "n")
    ]

    while reduced:
        reduced = False
        for pair in rules:
            x, y, rep = pair
            #print directions, x, y, rep
            if x in directions and y in directions:
                #print "found!"
                reduced = True
                min_occurances = min(directions.count(x), directions.count(y))
                #print "replacing %d instances of %s and %s" % (min_occurances, x, y),
                directions = listReplace(directions, x, "", min_occurances)
                directions = listReplace(directions, y, "", min_occurances)
                if rep != "":
                    for i in range(0, min_occurances):
                        directions.append(rep)

    return directions


def part1():
    with open("input.txt") as f:
        for line in f:
            directions = line.strip().split(",")
            reduced = reduce(directions)
            print "Part1:", len(reduced)

def part2():
    with open("input.txt") as f:
        for line in f:
            directions = line.strip().split(",")
            maxDistance = 0
            for i in range(1, len(directions)+1):
                step = directions[0:i]
                dist = len(reduce(step))
                if dist > maxDistance:
                    maxDistance = dist
            print "Part2:", maxDistance

part1()
part2()