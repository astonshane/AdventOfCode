from register import register_solution

def to_set(t):
    [i,j] = [int(x) for x in t.split('-')]
    return set(range(i, j+1))

@register_solution(2022, 4, 1)
@register_solution(2022, 4, 2)
def part1(filepath):
    with open(filepath) as f:
        fully_contained = 0
        any_overlap = 0

        for line in f:
            line = line.strip().split(',')
            r1 = to_set(line[0])
            r2 = to_set(line[1])

            u = r1.union(r2)
            if u == r1 or u == r2:
                fully_contained += 1
            if len(u) != len(r1) + len(r2):
                any_overlap += 1
        
        print("Part1:", fully_contained)
        print("Part2:", any_overlap)
