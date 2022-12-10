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


compressed = open('inputs/day9.txt').read().strip()
print "(part1):", decompress(compressed, False)
print "(part2):", decompress(compressed, True)
