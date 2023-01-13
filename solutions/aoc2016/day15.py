from register import register_solution
import re

def run(filename, part_2):
    with open(filename) as f:
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

        if part_2:
            discs[len(discs) + 1] = {
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
                print("valid time:", time)
                break

            time += 1


@register_solution(2016, 15, 1)
def part1(filename):
    run(filename, False)


@register_solution(2016, 15, 2)
def part2(filename):
    run(filename, True)
