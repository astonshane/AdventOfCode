f = open('aunt_list.txt')
sues = {}
for line in f:
    line = line.strip().split(': ', 1)
    sue = int(line[0].split(' ')[1])
    sues[sue] = {}
    properties = line[1].split(', ')
    for prop in properties:
        prop = prop.split(': ')
        sues[sue][prop[0]] = int(prop[1])
    print sue, sues[sue]
f.close()

f = open('chal31_input.txt')
for line in f:
    line = line.split(': ')
    prop = line[0]
    value = int(line[1])
    to_remove = []
    for sue in sues:
        if prop in sues[sue]:
            if sues[sue][prop] != value:
                to_remove.append(sue)
    for sue in to_remove:
        del sues[sue]

print sues
