from register import register_solution


def countSafe(row):
    count = 0
    for c in row:
        if c == '.':
            count += 1
    return count


def run(previous_row, NUM_ROWS):
    rows = 1
    safe_pos = countSafe(previous_row)

    while rows != NUM_ROWS:
        new_row = ""
        for i in range(0, len(previous_row)):
            left = (previous_row[i-1] == '^') if i>0 else False
            center = previous_row[i] == '^'
            right = (previous_row[i+1] == '^') if i<len(previous_row)-1 else False

            nxt = (left and center and not right)
            nxt = nxt or (center and right and not left)
            nxt = nxt or (left and not center and not right)
            nxt = nxt or (right and not left and not center)

            new_row += '^' if nxt else '.'

        previous_row = new_row
        safe_pos += countSafe(previous_row)
        rows += 1

    return safe_pos


@register_solution(2016, 18, 1)
def part1(filename):
    with open(filename) as f:
        previous_row = f.read().strip()
        print(run(previous_row, 40))

@register_solution(2016, 18, 2)
def part2(filename):
    with open(filename) as f:
        previous_row = f.read().strip()
        print(run(previous_row, 400000))
