with open("inputs/day2.txt") as f:
    depth = 0
    horizontal = 0

    for line in f:
        line = line.strip().split()
        line[1] = int(line[1])

        if line[0] == "forward":
            horizontal += line[1]
        elif line[0] == "up":
            depth -= line[1]
        elif line[0] == "down":
            depth += line[1]
    
    print("depth:", depth)
    print("horizontal:", horizontal)
    print("part1:", depth*horizontal)

with open("inputs/day2.txt") as f:
    depth = 0
    horizontal = 0
    aim = 0

    for line in f:
        line = line.strip().split()
        line[1] = int(line[1])

        if line[0] == "forward":
            horizontal += line[1]
            depth += aim*line[1]
        elif line[0] == "up":
            aim -= line[1]
        elif line[0] == "down":
            aim += line[1]
    
    print("aim:", aim)
    print("depth:", depth)
    print("horizontal:", horizontal)
    print("part2:", depth*horizontal)