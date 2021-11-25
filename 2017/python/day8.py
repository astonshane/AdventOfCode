import re

registers = {}
MAX_VAL = 0

def get_register(name):
    return registers.get(name, 0)

def update_register(register, value, command):
    new_val = None
    if command == "inc":
        new_val = get_register(register) + int(value)
    else:
        new_val = get_register(register) - int(value)
    
    global MAX_VAL
    MAX_VAL = max(MAX_VAL, new_val)
    
    registers[register] = new_val

instruction_re = re.compile("([a-z]+) (inc|dec) (-*\d+) if ([a-z]+) (.+ -*\d+)")
with open("inputs/day8.txt") as f:
    for line in f:
        line = line.strip()
        (register, command, value, condition_register, condition) = instruction_re.match(line).groups()

        expression = "%d %s" % (get_register(condition_register), condition)
        if eval(expression):
            update_register(register, value, command)
        
print("part1:", max(registers.values()))
print("part2:", MAX_VAL)