import sys
import copy
from random import shuffle

# ######################
if len(sys.argv) != 2:
    print "need an input file"
    exit(1)

f = open(sys.argv[1])
transitions = []

mol = None

for line in f:
    line = line.strip()
    if "=>" in line:
        line = line.split("=>")
        start = line[0].strip()
        end = line[1].strip()
        transitions.append((end, start))
    else:
        mol = line

transitions.sort(lambda x, y: cmp(len(x[0]), len(y[0])), reverse=True)
count = 0
while mol != 'e':
    for frm, to in transitions:
        if frm in mol:
            mol = mol.replace(frm, to, 1)
            count += 1
print count
