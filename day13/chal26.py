import sys
import itertools

hUnits = {}


def findHappiness(arrangment):
    happiness = 0
    for i in range(0, len(arrangment)):
        person = arrangment[i]
        personLeft, personRight = None, None
        if i == 0:
            personLeft = arrangment[-1]
        else:
            personLeft = arrangment[i-1]

        if i == len(arrangment) - 1:
            personRight = arrangment[0]
        else:
            personRight = arrangment[i+1]

        happiness += hUnits[person][personLeft] + hUnits[person][personRight]
    return happiness

# ######################
if len(sys.argv) != 2:
    print "need an input file"
    exit(1)

f = open(sys.argv[1])

# parse the file
for line in f:
    line = line.strip(" \n.").split()
    person1 = line[0]
    person2 = line[-1]
    units = int(line[3])
    if line[2] == 'lose':
        units *= -1

    if person1 not in hUnits:
        hUnits[person1] = {}
    hUnits[person1][person2] = units

# add 'me' to the list
users = hUnits.keys()
hUnits['me'] = {}
for user in users:
    hUnits['me'][user] = 0
    hUnits[user]['me'] = 0

print hUnits
max_happy = None
allPerms = itertools.permutations(hUnits.keys())
for perm in allPerms:
    tmp = findHappiness(perm)
    if max_happy is None or tmp > max_happy:
        max_happy = tmp

print "max_happiness:", max_happy
