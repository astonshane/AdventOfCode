from register import register_solution


def decompress(compressed, part2):
    retval = 0
    while '(' in compressed:
        open_paren = compressed.find('(')
        retval += open_paren
        compressed = compressed[open_paren:]

        closed_paren = compressed.find(')')
        marker = compressed[1:closed_paren].split('x')
        compressed = compressed[closed_paren + 1:]

        length, mult = int(marker[0]), int(marker[1])

        if part2:
            retval += decompress(compressed[:length], part2) * mult
        else:
            retval += length * mult
        compressed = compressed[length:]
    retval += len(compressed)
    return retval


@register_solution(2016, 9, 1)
def part1(filename):
    compressed = open(filename).read().strip()
    print(decompress(compressed, False))


@register_solution(2016, 9, 2)
def part2(filename):
    compressed = open(filename).read().strip()
    print(decompress(compressed, True))
