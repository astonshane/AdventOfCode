f = open("chal5_input.txt")
pos = (0,0)
count = set()
for line in f:
    for c in line.strip():
        count.add(pos)
        print pos, c,
        if c == '>':
            pos = (pos[0]+1, pos[1])
        elif c == "<":
            pos = (pos[0]-1, pos[1])
        elif c == "^":
            pos = (pos[0], pos[1]+1)
        elif c == "v":
            pos = (pos[0], pos[1]-1)
        print pos

count.add(pos)
# print count
print len(count)
