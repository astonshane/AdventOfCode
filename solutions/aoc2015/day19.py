from register import register_solution


@register_solution(2015, 19, 1)
def part1(filename):
    with open(filename) as f:
        transitions = {}

        starting = None

        for line in f:
            line = line.strip()
            if "=>" in line:
                line = line.split("=>")
                start = line[0].strip()
                end = line[1].strip()
                if start not in transitions:
                    transitions[start] = []
                transitions[start].append(end)
            else:
                starting = line

        molecules = set()
        for i in range(0, len(starting)):
            for base in transitions:
                if starting[i:i + len(base)] == base:
                    for transition in transitions[base]:
                        new = starting[:i] + transition + starting[i + len(base):]
                        molecules.add(new)
        print(len(molecules))


@register_solution(2015, 19, 2)
def part2(filename):
    with open(filename) as f:
        transitions = []

        mol = None

        for line in f:
            line = line.strip()
            if "=>" in line:
                line = line.split("=>")
                start = line[0].strip()
                end = line[1].strip()
                transitions.append((end, start))
            else:
                mol = line

        #transitions.sort(lambda x, y: cmp(len(x[0]), len(y[0])), reverse=True)
        transitions.sort(reverse=True, key=lambda x: len(x[0]))
        count = 0
        while mol != 'e':
            for frm, to in transitions:
                if frm in mol:
                    mol = mol.replace(frm, to, 1)
                    count += 1
        print(count)
