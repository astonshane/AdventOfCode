f = open('chal1_input.txt')
floor = 0
for line in f:
    for c in line:
        if c == "(":
            print "("
            floor += 1
        elif c == ")":
            print ")"
            floor -= 1

print floor
