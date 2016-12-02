def part1():
    f = open('inputs/day1.txt')
    x = 0
    y = 0

    '''
    0 == N
    1 == N+1 == S-1 == E
    2 == S
    3 == W
    '''
    facing = 0

    for line in f:
        for instruction in line.split(","):
            instruction = instruction.strip()
            direction = instruction[0]
            distance = int(instruction[1:])

            if direction == "R":
                facing = (facing + 1) % 4
            else:
                facing = (facing -1) % 4


            if facing == 0:
                y += distance
            elif facing == 1:
                x += distance
            elif facing == 2:
                y -= distance
            elif facing == 3:
                x -= distance

    print "(part1): distance from start: ", abs(x) + abs(y)

def part2():
    visited = set()
    visited.add((0,0))

    current_set_size = len(visited)

    f = open('inputs/day1.txt')
    x = 0
    y = 0

    '''
    0 == N
    1 == N+1 == S-1 == E
    2 == S
    3 == W
    '''
    facing = 0

    found = False

    for line in f:
        for instruction in line.split(","):
            instruction = instruction.strip()
            direction = instruction[0]
            distance = int(instruction[1:])

            if direction == "R":
                facing = (facing + 1) % 4
            else:
                facing = (facing -1) % 4

            current = (x, y)
            print current
            final = None

            if facing == 0:
                final = (x, y+distance)
            elif facing == 1:
                final = (x+distance, y)
            elif facing == 2:
                final = (x, y-distance)
            elif facing == 3:
                final = (x+distance, y)

            for i in range(1, distance+1):
                if facing == 0:
                    current = (current[0], current[1]+1)
                elif facing == 1:
                    current = (current[0]+1, current[1])
                elif facing == 2:
                    current = (current[0], current[1]-1)
                elif facing == 3:
                    current = (current[0]-1, current[1])

                print current, visited


                if current in visited:
                    print "part2: ", current, abs(current[0]) + abs(current[1])
                    found = True
                    break
                else:
                    visited.add(current)

            if found:
                break


            x = current[0]
            y = current[1]
#part1()
part2()
