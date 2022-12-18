from register import register_solution


def parse_input(filepath):
    with open(filepath) as f:
        elves = []
        current_elf = []

        for line in f:
            line = line.strip()
            if not line:
                elves.append(current_elf)
                current_elf = []
            else:
                current_elf.append(int(line))
        elves.append(current_elf)
        return elves


@register_solution(2022, 1, 1)
def part1(filepath):
    elves = parse_input(filepath)
    print("Answer:", max([sum(x) for x in elves]))


@register_solution(2022, 1, 2)
def part2(filepath):
    elves = parse_input(filepath)
    elves = [sum(x) for x in elves]
    elves.sort(reverse=True)
    print("Answer:", sum(elves[:3]))
