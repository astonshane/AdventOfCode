from collections import deque
NUM_ELVES = 3014387

def part1():
    elves = []
    for i in range(1, NUM_ELVES+1):
        elves.append((i, True))

    while len(elves) > 1:
        for i in range(0, len(elves)):
            cur = elves[i]
            if cur[1]:
                nxt = elves[(i+1) % len(elves)]
                elves[(i+1) % len(elves)] = (nxt[0], False)

        new_elves = []
        for elf in elves:
            if elf[1]:
                new_elves.append(elf)
        elves = new_elves
    print "(part1):", elves[0][0]

def part2():
    l = deque()
    r = deque()

    # split the initial list in half
    for i in range(1, NUM_ELVES+1):
        if i < (NUM_ELVES//2)+1:
            l.append(i)
        else:
            r.append(i)

    while l and r:
        if len(l) > len(r):
            l.pop()
        else:
            r.pop()

        # rotate the lists:
        r.appendleft(l.popleft())
        l.append(r.pop())

    print "(part2):", l[0] or r[0]

# part1
part2()
