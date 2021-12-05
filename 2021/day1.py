with open("inputs/day1.txt") as f:
    lines = f.readlines()
    lines = [int(x.strip()) for x in lines]

    increasing = 0
    for i in range(1, len(lines)):
        if lines[i] > lines[i-1]:
            increasing += 1
    print("part1:", increasing)


    increasing = 0
    previous = None
    for i in range(0, len(lines)-2):
        current = sum(lines[i:i+3])
        if previous is not None:
            if current > previous:
                increasing += 1
        
        previous = current
    print("part2:", increasing)