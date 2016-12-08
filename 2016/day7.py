def part1():
    f = open("inputs/day7.txt")
    tls_count = 0

    for line in f:
        inner = False
        line = line.strip()

        abba_inner = False
        abba_outer = False

        for i in range(0, len(line)-3):
            if line[i] == "[":
                inner = True
                continue
            elif line[i] == "]":
                inner = False
                continue

            a, b = line[i]+line[i+1], line[i+3]+line[i+2]
            if a == b and a[0] != a[1]:
                if inner:
                    abba_inner = True
                    break
                else:
                    abba_outer = True

        if abba_outer and (not abba_inner):
            tls_count += 1
    print "(part1):", tls_count

def part2():
    f = open("inputs/day7.txt")
    ssl_count = 0

    for line in f:
        inner = False
        line = line.strip()

        supernet = []
        hypernet = []

        for i in range(0, len(line)-2):
            if line[i] == "[":
                inner = True
                continue
            elif line[i] == "]":
                inner = False
                continue

            aba = line[i:i+3]
            if '[' not in aba and ']' not in aba and aba[0] == aba[2] and aba[0] != aba[1]:
                if inner:
                    hypernet.append(aba)
                else:
                    supernet.append(aba)
        for aba in supernet:
            bab = aba[1] + aba[0] + aba[1]
            if bab in hypernet:
                ssl_count += 1
                break
    print "(part2):", ssl_count

part1()
part2()
