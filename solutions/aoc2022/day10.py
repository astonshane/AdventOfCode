from register import register_solution


@register_solution(2022, 10, 1)
def part1(filename):
    commands = []
    with open(filename) as f:
        for line in f:
            commands.append(line.strip().split())

    register_x = 1
    cycle = 1
    signal_strength = 0

    to_add = None
    while True:
        if cycle in [20, 60, 100, 140, 180, 220]:
            print("Start of cycle %d. X == %d" % (cycle, register_x))
            signal_strength += cycle * register_x

        if to_add is not None:
            register_x += to_add
            to_add = None
        else:
            if len(commands) == 0:
                break
            command = commands.pop(0)
            #print(command)

            if command[0] == 'addx':
                to_add = int(command[1])

        cycle += 1

    print("Signal Strength:", signal_strength)






@register_solution(2022, 10, 2)
def part2(filename):
    commands = []
    with open(filename) as f:
        for line in f:
            commands.append(line.strip().split())

    register_x = 1
    draw_pos = 0
    current_line = ""

    to_add = None
    while True:
        # print("Draw Pos %d. X == %d" % (draw_pos, register_x))

        if draw_pos in [register_x, register_x-1, register_x+1]:
            current_line += '#'
        else:
            current_line += ' '

        if len(current_line) == 40:
            print(current_line)
            current_line = ""
            draw_pos = -1

        if to_add is not None:
            register_x += to_add
            to_add = None
        else:
            if len(commands) == 0:
                break
            command = commands.pop(0)

            if command[0] == 'addx':
                to_add = int(command[1])

        draw_pos += 1
