def day1():
    f = open("inputs/day2.txt")

    '''
    123
    456
    789
    '''

    code = ""
    pos = 5

    for line in f:
        line = line.strip()
        for inst in line:
            if inst == "L" and pos not in [1, 4, 7]:
                pos -= 1
            elif inst == "R" and pos not in [3, 6, 9]:
                pos += 1
            elif inst == "U" and pos not in [1, 2, 3]:
                pos -= 3
            elif inst == "D" and pos not in [7, 8, 9]:
                pos += 3
        code += str(pos)
    print "(Part 1):", code


def day2():
    '''
        1
      2 3 4
    5 6 7 8 9
      A B C
        D
    '''

    f = open("inputs/day2.txt")

    code = ""
    pos = 5

    for line in f:
        line = line.strip()
        for inst in line:
            if inst == "L" and pos not in [1, 2, 5, 10, 13]:
                pos -= 1
            elif inst == "R" and pos not in [1, 4, 9, 12, 13]:
                pos += 1
            elif inst == "U" and pos not in [1, 2, 4, 5, 9]:
                if pos == 3 or pos == 13:
                    pos -= 2
                else:
                    pos -= 4
            elif inst == "D" and pos not in [5, 9, 10, 12, 13]:
                if pos == 1 or pos == 11:
                    pos += 2
                else:
                    pos += 4

        translated = ['A', 'B', 'C', 'D']
        if pos < 10:
            code += str(pos)
        else:
            code += translated[pos%10]


    print "(Part 2):", code
day1()
day2()
