from register import register_solution

priorities = {}
for i in range(0, 26):
    priorities[ord('a') + i] = 1 + i
    priorities[ord('A') + i] = 27 + i


@register_solution(2022, 3, 1)
def part1(filepath):
    with open(filepath) as f:
        total_priority = 0
        for line in f:
            line = line.strip()
            midway = int(len(line)/2)
            compartment1 = set(line[:midway])
            compartment2 = set(line[midway:])
            item = list(compartment1.intersection(compartment2))[0]
            priority = priorities[ord(item)]
            total_priority += priority
        print("Answer:", total_priority)


@register_solution(2022, 3, 2)
def part2(filepath):
    with open(filepath) as f:
        total_priority = 0
        current = []
        for line in f:
            line = set(line.strip())
            current.append(line)
            if len(current) == 3:
                item = list(current[0].intersection(current[1]).intersection(current[2]))[0]
                priority = priorities[ord(item)]
                total_priority += priority
                current = []
        print("Answer:", total_priority)
            