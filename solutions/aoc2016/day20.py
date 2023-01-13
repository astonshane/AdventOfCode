from register import register_solution

def parse_input(filename):
    blacklist = []
    with open(filename) as f:
        for line in f:
            line = line.strip().split('-')
            blacklist.append([int(x) for x in line])

    blacklist.sort()
    return blacklist

@register_solution(2016, 20, 1)
def part1(filename):
    blacklist = parse_input(filename)
    ip = 0
    for i in range(0, len(blacklist)):
        bl = blacklist[i]

        if ip < bl[0]:
            break
        if bl[1] > ip:
            ip = bl[1] + 1
    print(ip)



@register_solution(2016, 20, 2)
def part2(filename):
    blacklist = parse_input(filename)
    ip = 0
    good_ips = 0
    for i in range(0, len(blacklist)):
        bl = blacklist[i]

        if ip < bl[0]:
            good_ips += bl[0]-ip
            ip = bl[1]+1
        elif bl[1] > ip:
            ip = bl[1]+1
    print(good_ips)