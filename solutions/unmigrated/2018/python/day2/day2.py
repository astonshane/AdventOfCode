def getCounts(line):
    line = sorted(line)
    counts = {}
    for c in line:
        counts[c] = counts.get(c, 0) + 1

    return 2 in counts.values(), 3 in counts.values()

def part1():
    lines = []
    with open("input.txt") as f:
        for line in f:
            lines.append(line.strip())
    two_count = 0
    three_count = 0

    for line in lines:
        two, three = getCounts(line)
        two_count += int(two)
        three_count += int(three)

    print "part1():", two_count*three_count

def part2():
    lines = []
    with open("input.txt") as f:
        for line in f:
            lines.append(line.strip())
    
    found = False
    for i in range(0, len(lines)):
        a = lines[i]
        for j in range(i+1, len(lines)):
            b = lines[j]
            
            shared = ""
            for k in range(0, len(a)):
                if a[k] == b[k]:
                    shared += a[k]
            if len(shared) == len(a)-1:
                found = True
                print "part2:", shared
                break
        if found:
            break



part1()
part2()