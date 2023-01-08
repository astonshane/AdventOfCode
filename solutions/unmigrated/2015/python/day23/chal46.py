import sys

'''
    - hlf r sets register r to half its current value, then continues with the next instruction.
    - tpl r sets register r to triple its current value, then continues with the next instruction.
    - inc r increments register r, adding 1 to it, then continues with the next instruction.
    - jmp offset is a jump; it continues with the instruction offset away relative to itself.
    - jie r, offset is like jmp, but only jumps if register r is even ("jump if even").
    - jio r, offset is like jmp, but only jumps if register r is 1 ("jump if one", not odd).
'''

# ######################
if len(sys.argv) != 2:
    print "need an input file"
    exit(1)

f = open(sys.argv[1])

instructions = []


for line in f:
    instructions.append(line.strip().split())
print instructions

registers = {'a': 1, 'b': 0}
i = 0
while (i < len(instructions)):
    inst = instructions[i]
    print i, registers, inst
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
        if registers[r]  == 1:
            i += offset
        else:
             i += 1

print "a: %d, b: %d" % (registers['a'], registers['b'])
