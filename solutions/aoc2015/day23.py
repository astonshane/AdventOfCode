from register import register_solution

'''
    - hlf r sets register r to half its current value, then continues with the next instruction.
    - tpl r sets register r to triple its current value, then continues with the next instruction.
    - inc r increments register r, adding 1 to it, then continues with the next instruction.
    - jmp offset is a jump; it continues with the instruction offset away relative to itself.
    - jie r, offset is like jmp, but only jumps if register r is even ("jump if even").
    - jio r, offset is like jmp, but only jumps if register r is 1 ("jump if one", not odd).
'''

def run(filename, registers):
    instructions = []
    with open(filename) as f:
        for line in f:
            instructions.append(line.strip().split())
    i = 0
    while i < len(instructions):
        inst = instructions[i]
        #print(i, registers, inst)
        if inst[0] == "hlf":
            registers[inst[1]] = registers[inst[1]] / 2
            i += 1
        elif inst[0] == "tpl":
            registers[inst[1]] = registers[inst[1]] * 3
            i += 1
        elif inst[0] == "inc":
            registers[inst[1]] = registers[inst[1]] + 1
            i += 1
        elif inst[0] == "jmp":
            i += int(inst[1])
        elif inst[0] == "jie":
            offset = int(inst[-1])
            r = inst[1].strip(',')
            if registers[r] % 2 == 0:
                i += offset
            else:
                i += 1
        elif inst[0] == "jio":
            offset = int(inst[-1])
            r = inst[1].strip(',')
            if registers[r] == 1:
                i += offset
            else:
                i += 1

    return registers['b']


@register_solution(2015, 23, 1)
def part1(filename):
    registers = {'a': 0, 'b': 0}
    print(run(filename, registers))


@register_solution(2015, 23, 2)
def part2(filename):
    registers = {'a': 1, 'b': 0}
    print(run(filename, registers))


