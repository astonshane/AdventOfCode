import sys
from itertools import combinations


def sumCombo(combo):
    total = 0
    for i in combo:
        total += i
    return total

# ######################
if len(sys.argv) != 3:
    print "need an input file and storage capacity"
    exit(1)
storage = int(sys.argv[2])

containers = []

f = open(sys.argv[1])
for line in f:
    containers.append(int(line.strip()))

total_combos = 0

for i in range(0, len(containers)):
    for combo in combinations(containers, i):
        if sumCombo(combo) == storage:
            total_combos += 1

print total_combos
