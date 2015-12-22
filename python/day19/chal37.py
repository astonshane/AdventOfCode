import sys

# ######################
if len(sys.argv) != 2:
    print "need an input file"
    exit(1)

f = open(sys.argv[1])
transitions = {}

starting = None

for line in f:
    line = line.strip()
    if "=>" in line:
        line = line.split("=>")
        start = line[0].strip()
        end = line[1].strip()
        if start not in transitions:
            transitions[start] = []
        transitions[start].append(end)
    else:
        starting = line

molecules = set()
for i in range(0, len(starting)):
    for base in transitions:
        if starting[i:i+len(base)] == base:
            for transition in transitions[base]:
                new = starting[:i] + transition + starting[i+len(base):]
                molecules.add(new)
print molecules, len(molecules)
