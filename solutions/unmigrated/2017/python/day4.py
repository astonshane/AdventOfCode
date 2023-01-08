with open("inputs/day4.txt") as f:
    count = 0
    for line in f:
        line = line.strip().split()
        if len(line) == len(set(line)):
            count += 1        
    print("part1:", count)

with open("inputs/day4.txt") as f:
    count = 0
    for line in f:
        line = line.strip().split()
        line = [''.join(sorted(x)) for x in line]
        if len(line) == len(set(line)):
            count += 1        
    print("part2:", count)