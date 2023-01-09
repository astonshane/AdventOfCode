from register import register_solution


@register_solution(2016, 7, 1)
def part1(filename):
    tls_count = 0
    with open(filename) as f:
        for line in f:
            inner = False
            line = line.strip()

            abba_inner = False
            abba_outer = False

            for i in range(0, len(line) - 3):
                if line[i] == "[":
                    inner = True
                    continue
                elif line[i] == "]":
                    inner = False
                    continue

                a, b = line[i] + line[i + 1], line[i + 3] + line[i + 2]
                if a == b and a[0] != a[1]:
                    if inner:
                        abba_inner = True
                        break
                    else:
                        abba_outer = True

            if abba_outer and (not abba_inner):
                tls_count += 1
    print(tls_count)


@register_solution(2016, 7, 2)
def part2(filename):
    ssl_count = 0

    with open(filename) as f:
        for line in f:
            inner = False
            line = line.strip()

            supernet = []
            hypernet = []

            for i in range(0, len(line) - 2):
                if line[i] == "[":
                    inner = True
                    continue
                elif line[i] == "]":
                    inner = False
                    continue

                aba = line[i:i + 3]
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
    print(ssl_count)
