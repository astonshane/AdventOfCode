MAX = 4294967295

blacklist = []
with open("inputs/day20.txt") as f:
    for line in f:
        line = line.strip().split('-')
        blacklist.append([int(x) for x in line])

blacklist.sort()

def part1():
    ip = 0
    for i in range(0, len(blacklist)):
        bl = blacklist[i]

        if ip < bl[0]:
            break
        if bl[1] > ip:
            ip = bl[1]+1



    print "(part1):", ip

def part2():
    ip = 0
    good_ips = 0
    for i in range(0, len(blacklist)):
        bl = blacklist[i]

        if ip < bl[0]:
            good_ips += bl[0]-ip
            ip = bl[1]+1
        elif bl[1] > ip:
            ip = bl[1]+1


    print "(part2):", good_ips

part1()
part2()
