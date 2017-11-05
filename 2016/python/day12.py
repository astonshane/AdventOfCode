import re

def run(registers):
    cpyRegisterRegex = 'cpy ([a-z]) ([a-z])'
    cpyValueRegex = 'cpy (\d+) ([a-z])'
    incDecRegex = '(inc|dec) ([a-z])'
    jnzValueRegex = 'jnz (\d+) (\-\d+|\d+)'
    jnzRegisterRegex = 'jnz ([a-z]) (\-\d+|\d+)'

    lines = []

    f = open('inputs/day12.txt')
    for line in f:
        lines.append(line.strip())

    i = 0
    while i < len(lines):
        line = lines[i]

        m = re.search(cpyValueRegex, line)
        if m != None:
            (value, register) = m.groups()
            registers[register] = int(value)
            i += 1
            continue

        m1 = re.search(cpyRegisterRegex, line)
        if m1 != None:
            (fromRegister, toRegister) = m1.groups()
            registers[toRegister] = registers[fromRegister]
            i += 1
            continue

        m2 = re.search(incDecRegex, line)
        if m2 != None:
            (kind, register) = m2.groups()
            mod = 0
            if kind == "inc":
                mod = 1
            else:
                mod = -1
            registers[register] += mod
            i += 1
            continue

        m3 = re.search(jnzValueRegex, line)
        if m3 != None:
            (tester, jump) = m3.groups()
            if int(tester) != 0:
                i += int(jump)
            else:
                i += 1
            continue

        m4 = re.search(jnzRegisterRegex, line)
        if m4 != None:
            (tester, jump) = m4.groups()
            if registers[tester] != 0:
                i += int(jump)
            else:
                i += 1
            continue

        assert(False)


    return registers['a']

registers = {'a':0, 'b':0, 'c':0, 'd':0}
print "(part1):", run(registers)
registers = {'a':0, 'b':0, 'c':1, 'd':0}
print "(part2):", run(registers)
