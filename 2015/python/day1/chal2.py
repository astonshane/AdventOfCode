f = open('chal1_input.txt')
floor = 0
i = 1
for line in f:
    for c in line:
        if c == "(":
            floor += 1
        elif c == ")":
            floor -= 1
        if floor < 0:
            print i
            break
        i += 1
