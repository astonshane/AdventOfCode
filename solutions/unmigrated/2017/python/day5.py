def process(part1=True):
    instructions = []
    with open("inputs/day5.txt") as f:
        for line in f:
            instructions.append(int(line))

    index = 0
    steps = 0

    while index in range(0, len(instructions)):
        new_index = index + instructions[index]
        if not part1 and instructions[index] >= 3:
            instructions[index] -= 1
        else:
            instructions[index] += 1
        index = new_index
        steps += 1

    return steps

print("part1:", process(part1=True))
print("part2:", process(part1=False))
