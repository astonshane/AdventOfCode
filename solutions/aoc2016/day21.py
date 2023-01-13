from register import register_solution
import re


swap_position = 'swap position (\d) with position (\d)'
swap_letter = 'swap letter ([a-z]) with letter ([a-z])'
rotate_lr = 'rotate (left|right) (\d) step[s]?'
rotate_on_pos = 'rotate based on position of letter ([a-z])'
reverse = 'reverse positions (\d) through (\d)'
move = 'move position (\d) to position (\d)'

test_pwd = list("fbgdceah")

def swapPosition(pwd, x, y, part2):
    # the letters at indexes X and Y (counting from 0) should be swapped
    tmp = pwd[x]
    pwd[x] = pwd[y]
    pwd[y] = tmp
    return pwd

scrambled = swapPosition(test_pwd, 0, 1, False)
unscrambled = swapPosition(scrambled, 0, 1, True)
assert(test_pwd == unscrambled)

def swapLetter(pwd, x, y, part2):
    # swap letter X with letter Y
    x_index = pwd.index(x)
    y_index = pwd.index(y)
    return swapPosition(pwd, x_index, y_index, part2)

scrambled = swapLetter(test_pwd, 'a', 'b', False)
unscrambled = swapLetter(scrambled, 'b', 'a', True)
assert(test_pwd == unscrambled)

def rotateLR(pwd, direction, steps, part2):
    # the whole string should be rotated left|right by a number of steps
    if part2:
        if direction == "right":
            direction = "left"
        else:
            direction = "right"
    direction = 1 if direction == "right" else -1
    new_pwd = pwd[:]
    for i in range(0, len(pwd)):
        new_i = (i + direction*steps) % len(pwd)
        new_pwd[new_i] = pwd[i]
    return new_pwd

scrambled = rotateLR(test_pwd, 'right', 3, False)
unscrambled = rotateLR(scrambled, 'right', 3, True)
assert(test_pwd == unscrambled)

def rotateOnPos(pwd, letter, part2):
    # the whole string should be rotated to the right based on the index of letter X (counting from 0)
    #   as determined before this instruction does any rotations. Once the index is determined,
    #   rotate the string to the right one time, plus a number of times equal to that index,
    #   plus one additional time if the index was at least 4
    if part2:
        rotated = rotateLR(pwd, "left", 1, False)
        while True:
            if rotateOnPos(rotated, letter, False) == pwd:
                return rotated
            rotated = rotateLR(rotated, "left", 1, False)

    else:
        index = pwd.index(letter)
        steps = index+1
        if index >= 4:
            steps += 1

        return rotateLR(pwd, "right", steps, part2)

scrambled = rotateOnPos(test_pwd, 'a', False)
unscrambled = rotateOnPos(scrambled, 'a', True)
assert(test_pwd == unscrambled)


def reversePositions(pwd, i, j, part2):
    # he span of letters at indexes X through Y (including the letters at X and Y) should be reversed in order
    before = pwd[:i]
    middle = pwd[i:j+1]
    middle.reverse()
    after = pwd[j+1:]
    new_pwd = before
    new_pwd.extend(middle)
    new_pwd.extend(after)
    return new_pwd

scrambled = reversePositions(test_pwd, 1, 3, False)
unscrambled = reversePositions(scrambled, 1, 3, True)
assert(test_pwd == unscrambled)


def movePos(pwd, x, y, part2):
    # move position X to position Y
    pwd = pwd[:]
    if part2:
        tmp = x
        x = y
        y = tmp
    val = pwd[x]
    pwd.remove(val)
    new_pwd = pwd[:y]
    new_pwd.append(val)
    new_pwd.extend(pwd[y:])
    assert(new_pwd[y] == val)
    return new_pwd

scrambled = movePos(test_pwd, 0, 1, False)
unscrambled = movePos(scrambled, 0, 1, True)
assert(test_pwd == unscrambled)


def run(filename, pwd, part2):
    steps = []
    with open(filename) as file:
        for line in file:
            steps.append(line.strip())

    if part2:
        steps.reverse()

    for line in steps:
        line = line.strip()

        m = re.search(swap_position, line)
        if m is not None:
            pwd = swapPosition(pwd, int(m.groups()[0]), int(m.groups()[1]), part2)
            continue

        m = re.search(swap_letter, line)
        if m is not None:
            pwd = swapLetter(pwd, m.groups()[0], m.groups()[1], part2)
            continue

        m = re.search(rotate_lr, line)
        if m is not None:
            pwd = rotateLR(pwd, m.groups()[0], int(m.groups()[1]), part2)
            continue

        m = re.search(rotate_on_pos, line)
        if m is not None:
            pwd = rotateOnPos(pwd, m.groups()[0], part2)
            continue

        m = re.search(reverse, line)
        if m is not None:
            pwd = reversePositions(pwd, int(m.groups()[0]), int(m.groups()[1]), part2)
            continue

        m = re.search(move, line)
        if m is not None:
            pwd = movePos(pwd, int(m.groups()[0]), int(m.groups()[1]), part2)
            continue
    return ''.join(pwd)


@register_solution(2016, 21, 1)
def part1(filename):
    print(run(filename, list("abcdefgh"), False))


@register_solution(2016, 21, 2)
def part2(filename):
    print(run(filename, list("fbgdceah"), True))
