import re

PART2 = True

with open('inputs/day15.txt') as f:
    discs = {}

    pttrn = 'Disc #(\d+) has (\d+) positions; at time=0, it is at position (\d+).'
    for line in f:
        m = re.search(pttrn, line.strip())
        if m is not None:
            group = [int(x) for x in m.groups()]
            disc, positions, start = group
            discs[disc] = {
                'positions': positions,
                'start': start
            }

    if PART2:
        discs[len(discs)+1] = {
            'positions': 11,
            'start': 0
        }

    time = 0
    while True:
        valid = True
        for key in discs:
            disc = discs[key]
            if (disc['start'] + time + key) % disc['positions'] != 0:
                valid = False
                break
        if valid:
            print "valid time:", time
            break


        time += 1
