from register import register_solution


@register_solution(2024, 1, 1)
def part1(filename):
    l1 = []
    l2 = []
    with open(filename) as f:
        for line in f:
            line = line.split()
            l1.append(int(line[0]))
            l2.append(int(line[1]))
    l1.sort()
    l2.sort()
    total = 0
    for i in range(0, len(l1)):
        total += abs(l1[i] - l2[i])
    print(total)


@register_solution(2024, 1, 2)
def part2(filename):
    l1 = []
    counts = {}
    with open(filename) as f:
        for line in f:
            line = line.split()
            l1.append(int(line[0]))
            y = int(line[1])
            if y in counts:
                counts[y] += 1
            else:
                counts[y] = 1
        similarity = 0
        for x in l1:
             similarity += x * counts.get(x, 0)
        print(similarity)
