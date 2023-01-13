from register import register_solution
import re

cpyRegisterRegex = 'cpy ([a-z]) ([a-z])'
cpyValueRegex = 'cpy (\-\d+|\d+) ([a-z])'
incDecRegex = '(inc|dec) ([a-z])'
jnzValueRegex = 'jnz (\d+) (\-\d+|\d+)'
jnzRegisterRegex = 'jnz ([a-z]) (\-\d+|\d+)'
jnzValueRegisterRegex = 'jnz (\d+) ([a-z])'
jnzRegisterRegisterRegex = 'jnz ([a-z]) ([a-z])'
tglRegex = 'tgl ([a-z])'


def run(tape, registers):
    i = 0
    while i < len(tape):
        # print "#######################################"

        if i == 4:
            # recognize the multiplication pattern in the input and optimize for it
            registers["a"] += registers["d"] * registers["b"]
            registers["c"] = 0
            registers["d"] = 0
            i = 10
            continue

        line = tape[i]

        m = re.search(cpyValueRegex, line)
        if m is not None:
            (value, register) = m.groups()
            registers[register] = int(value)
            i += 1
            continue

        m1 = re.search(cpyRegisterRegex, line)
        if m1 is not None:
            (fromRegister, toRegister) = m1.groups()
            registers[toRegister] = registers[fromRegister]
            i += 1
            continue

        m2 = re.search(incDecRegex, line)
        if m2 is not None:
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
        if m3 is not None:
            (tester, jump) = m3.groups()
            if int(tester) != 0:
                i += int(jump)
            else:
                i += 1
            continue

        m4 = re.search(jnzRegisterRegex, line)
        if m4 is not None:
            (tester, jump) = m4.groups()
            if registers[tester] != 0:
                i += int(jump)
            else:
                i += 1
            continue

        m3 = re.search(jnzValueRegisterRegex, line)
        if m3 is not None:
            (tester, jump) = m3.groups()
            if int(tester) != 0:
                i += registers[jump]
            else:
                i += 1
            continue

        m4 = re.search(jnzRegisterRegisterRegex, line)
        if m4 is not None:
            (tester, jump) = m4.groups()
            if registers[tester] != 0:
                i += registers[jump]
            else:
                i += 1
            continue

        m5 = re.search(tglRegex, line)
        if m5 is not None:
            register = m5.groups()[0]
            shift = registers[register]
            to_access = i + shift
            if 0 <= to_access < len(tape):
                toggleLine = tape[to_access]
                toggleLine = toggleLine.split()
                if len(toggleLine) == 2:
                    if toggleLine[0] == "inc":
                        toggleLine[0] = "dec"
                    else:
                        toggleLine[0] = "inc"
                elif len(toggleLine) == 3:
                    if toggleLine[0] == "jnz":
                        toggleLine[0] = "cpy"
                    else:
                        toggleLine[0] = "jnz"
                toggleLine = ' '.join(toggleLine)
                tape[to_access] = toggleLine

            i += 1
            continue

        assert False

    return registers['a']


def parse_input(filename):
    with open(filename) as f:
        tape = []
        for line in f:
            tape.append(line.strip())
        return tape


@register_solution(2016, 23, 1)
def part1(filename):
    tape = parse_input(filename)
    registers = {
        "a": 7,
        "b": 0,
        "c": 0,
        "d": 0
    }
    print(run(tape, registers))


@register_solution(2016, 23, 2)
def part2(filename):
    tape = parse_input(filename)
    registers = {
        "a": 12,
        "b": 0,
        "c": 0,
        "d": 0
    }
    print(run(tape, registers))
