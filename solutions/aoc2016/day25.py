from register import register_solution
import re
import copy


def run(tape, registers):
    i = 0
    last = 1
    outCount = 0
    while i < len(tape):
        if outCount > 100:
            return True
        instruction = tape[i]
        # print i, instruction, registers

        m = re.search('cpy ([a-z]|[0-9]+) ([a-z])', instruction)
        if m is not None:
            (value, register) = m.groups()
            tmp = registers.get(value)
            if tmp is None:
                value = int(value)
            else:
                value = tmp
            registers[register] = value
            i += 1
            continue

        m = re.search('(inc|dec) ([a-z])', instruction)
        if m is not None:
            (kind, register) = m.groups()
            if kind == "inc":
                registers[register] += 1
            else:
                registers[register] -= 1
            i += 1
            continue

        m = re.search('jnz ([a-z]|[0-9+]) (\-[0-9]+|[0-9]+)', instruction)
        if m is not None:
            (test, jmp) = m.groups()
            tmp = registers.get(test)
            if tmp is None:
                test = int(test)
            else:
                test = tmp
            jmp = int(jmp)

            if test != 0:
                i += jmp
            else:
                i += 1
            continue

        m = re.search('out ([a-z]|[0-9]+)', instruction)
        if m is not None:
            value = m.groups()[0]
            tmp = registers.get(value)
            if tmp is None:
                value = int(value)
            else:
                value = tmp
            outCount += 1

            if (last + value) == 1:
                last = value
            else:
                return False

            i += 1
            continue

        print("Unrecognized instruction: %s" % instruction)
        assert False
    return False


@register_solution(2016, 25, 1)
@register_solution(2016, 25, 2)
def part1(filename):
    with open(filename) as f:
        tape = []
        for line in f:
            tape.append(line.strip())

        a = 0
        while True:
            registers = {
                "a": a,
                "b": 0,
                "c": 0,
                "d": 0
            }

            ok = run(copy.copy(tape), registers)
            if ok:
                print("success at a == %d" % a)
                break

            a += 1
