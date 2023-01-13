from register import register_solution
from hashlib import md5
from queue import Queue


def run(part_1):
    PASS = "njfxhljp"
    cl = ['a']
    op = []

    for i in range(0, 10):
        cl.append(str(i))
    for i in range(ord('b'), ord('f') + 1):
        op.append(chr(i))

    queue = Queue()

    #             (x, y, STEPS TO THIS POINT)
    initial_pos = (1, 1, '')
    longest = 0

    queue.put(initial_pos)
    while not queue.empty():
        pos = queue.get()

        if pos[0] == 4 and pos[1] == 4:
            if part_1:
                print(pos[2])
                break
            else:
                if len(pos[2]) > longest:
                    longest = len(pos[2])
                continue

        m = md5((PASS + pos[2]).encode())

        digest = m.hexdigest()[:4]
        dirs = ['U', 'D', 'L', 'R']
        for i in range(0, 4):
            if digest[i] in op:
                new_pos = None
                if dirs[i] == 'U' and (pos[1] - 1 > 0):
                    new_pos = (pos[0], pos[1] - 1, pos[2] + 'U')
                elif dirs[i] == 'D' and (pos[1] + 1 < 5):
                    new_pos = (pos[0], pos[1] + 1, pos[2] + 'D')
                elif dirs[i] == 'L' and (pos[0] - 1 > 0):
                    new_pos = (pos[0] - 1, pos[1], pos[2] + 'L')
                elif dirs[i] == 'R' and (pos[0] + 1 < 5):
                    new_pos = (pos[0] + 1, pos[1], pos[2] + 'R')

                if new_pos is not None:
                    queue.put(new_pos)

    print(longest)


@register_solution(2016, 17, 1)
def part1(filename):
    run(True)


@register_solution(2016, 17, 2)
def part2(filename):
    run(False)
