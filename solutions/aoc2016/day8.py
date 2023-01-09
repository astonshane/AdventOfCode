from register import register_solution
import re


def printScreen(screen):
    print("")
    for row in screen:
        print(''.join(row))
    print("")


def countScreen(screen):
    count = 0
    for row in screen:
        for spot in row:
            if spot == "#":
                count += 1
    return count


@register_solution(2016, 8, 1)
@register_solution(2016, 8, 2)
def part1(filename):
    f = open(filename)
    dimx = 50
    dimy = 6

    screen = [[]] * dimy
    for i in range(0, len(screen)):
        screen[i] = ['.'] * dimx

    for line in f:
        rectRegex = 'rect (\d+)x(\d+)'
        rotateRegex = 'rotate (column|row) [xy]=(\d+) by (\d+)'

        m = re.search(rectRegex, line)
        if m != None:
            x, y = int(m.groups()[0]), int(m.groups()[1])
            for j in range(0, y):
                for i in range(0, x):
                    screen[j][i] = '#'

        else:
            m = re.search(rotateRegex, line)
            if m != None:
                toRotate, which, by = m.groups()[0], int(m.groups()[1]), int(m.groups()[2])
                if toRotate == "column":
                    currentColumn = []

                    for j in range(0, len(screen)):
                        currentColumn.append(screen[j][which])
                    newColumn = [' '] * len(currentColumn)
                    for x in range(0, len(currentColumn)):
                        newColumn[(x + by) % len(currentColumn)] = currentColumn[x]

                    for j in range(0, len(screen)):
                        screen[j][which] = newColumn[j]
                else:
                    currentRow = screen[which]
                    newRow = [' '] * len(currentRow)
                    for x in range(0, len(currentRow)):
                        newRow[(x + by) % len(currentRow)] = currentRow[x]
                    screen[which] = newRow

    print("(part1):", countScreen(screen))
    print("(part2)")
    printScreen(screen)


@register_solution(2016, 8, 2)
def part2(filename):
    pass
