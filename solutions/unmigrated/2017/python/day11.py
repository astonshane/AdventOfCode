rules = [
    ("n", "s", None),
    ("ne", "sw", None),
    ("nw", "se", None),
    ("ne", "s", "se"),
    ("se", "n", "ne"),
    ("nw", "s", "sw"),
    ("sw", "n", "nw"),
    ("se", "sw", "s"),
    ("ne", "nw", "n")
]

def reduce(instructions):
    length = len(instructions)
    while True:
        for (a,b,replace) in rules:
            if a in instructions and b in instructions:
                instructions.remove(a)
                instructions.remove(b)
                if replace is not None:
                    instructions.append(replace)
        new_length = len(instructions)
        if new_length < length:
            length = new_length
        else:
            break
    return instructions


# more efficent way to do part 1
'''with open("inputs/day11.txt") as f:
    for line in f:
        instructions = line.strip().split(",")
        instructions = reduce(instructions)
        print("part1:", len(instructions))
'''


with open("inputs/day11.txt") as f:
    for line in f:
        instructions = line.strip().split(",")
        max_distance = 0
        path = []
        for instruction in instructions:
            path.append(instruction)
            path = reduce(path)
            max_distance = max(max_distance, len(path))
        print("part1:", len(path))
        print("part2:", max_distance)