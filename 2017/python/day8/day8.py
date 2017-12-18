import sys
import re

filename = sys.argv[1]
with open(filename) as input:

    registers = {}
    highestEver = 0

    for line in input:
        line = line.strip()
        regex = r"(.+) (inc|dec) (-?\d+) if (.+) (.+) (-?\d+)"
        matches = re.findall(regex, line)[0]

        register = matches[0]
        cmd = matches[1]

        (register, cmd, amount, test, op, testVal) = matches
        amount = int(amount)
        testVal = int(testVal)

        registerValue = registers.get(register, 0)
        testReg = registers.get(test, 0)

        valid = False
        if op == ">":
            valid = testReg > testVal
        elif op == "<":
            valid = testReg < testVal
        elif op == ">=":
            valid = testReg >= testVal
        elif op == "<=":
            valid = testReg <= testVal
        elif op == "==":
            valid = testReg == testVal
        elif op == "!=":
            valid = testReg != testVal

        if valid:
            if cmd == "inc":
                registers[register] = registerValue + amount
            else:
                registers[register] = registerValue - amount

            if registers[register] > highestEver:
                highestEver = registers[register]

    highest = None
    for register in registers:
        if highest is None:
            highest = register
        else:
            if registers[register] > registers[highest]:
                highest = register
    print "Part1:", highest, registers[highest]
    print "Part2:", highestEver
