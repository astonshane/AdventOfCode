from register import register_solution


def get_sues(filename):
    sues = {}
    with open(filename) as f:
        for line in f:
            line = line.strip().split(': ', 1)
            sue = int(line[0].split(' ')[1])
            sues[sue] = {}
            properties = line[1].split(', ')
            for prop in properties:
                prop = prop.split(': ')
                sues[sue][prop[0]] = int(prop[1])
    return sues


clues = [
    "children: 3",
    "cats: 7",
    "samoyeds: 2",
    "pomeranians: 3",
    "akitas: 0",
    "vizslas: 0",
    "goldfish: 5",
    "trees: 3",
    "cars: 2",
    "perfumes: 1",
]


@register_solution(2015, 16, 1)
def part1(filename):
    sues = get_sues(filename)
    for line in clues:
        line = line.split(': ')
        prop = line[0]
        value = int(line[1])
        to_remove = []
        for sue in sues:
            if prop in sues[sue]:
                if sues[sue][prop] != value:
                    to_remove.append(sue)
        for sue in to_remove:
            del sues[sue]

    print(list(sues.keys())[0])


@register_solution(2015, 16, 2)
def part2(filename):
    sues = get_sues(filename)
    for line in clues:
        line = line.split(': ')
        prop = line[0]
        value = int(line[1])
        to_remove = []
        for sue in sues:
            if prop in sues[sue]:
                if prop in ['cats', 'trees']:
                    if sues[sue][prop] > value:
                        continue
                elif prop in ['pomeranians', 'goldfish']:
                    if sues[sue][prop] < value:
                        continue
                elif sues[sue][prop] == value:
                    continue
                to_remove.append(sue)
        for sue in to_remove:
            del sues[sue]

    print(list(sues.keys())[0])