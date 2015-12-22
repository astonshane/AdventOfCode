import sys
import copy

# ######################
if len(sys.argv) != 3:
    print "need an input file and max teaspoons"
    exit(1)

ingredients = {}
max_teaspoons = int(sys.argv[2])

permutations = []


def assignValues(assignments, remainingKeys, assigned):
    toAssign = remainingKeys[0]
    remainingKeys.remove(toAssign)
    if len(remainingKeys) == 0:
        assignments[toAssign] = max_teaspoons - assigned
        permutations.append(assignments)
    else:
        for i in range(0, max_teaspoons-assigned+1):
            newAssignments = copy.copy(assignments)
            newAssignments[toAssign] = i
            assignValues(newAssignments, copy.copy(remainingKeys), assigned+i)


def score(assignment, catagories):
    score = 1
    for cat in catagories:
        cat_score = 0
        for ingredient in assignment:
            cat_score += ingredients[ingredient][cat] * assignment[ingredient]
        if cat_score < 0:
            score *= 0
        else:
            score *= cat_score
    return score


f = open(sys.argv[1])
for line in f:
    line = line.strip().split(":")
    ingredient = line[0]
    properties = line[1].split(',')
    props = {}
    for prop in properties:
        prop = prop.strip().split(' ')
        props[prop[0]] = int(prop[1])

    ingredients[ingredient] = props

keys = ingredients.keys()
assignValues({}, keys, 0)

max_score = None

catagories = ingredients[ingredients.keys()[0]].keys()
catagories.remove('calories')

for p in permutations:
    s = score(p, catagories)
    if max_score is None or s > max_score:
        max_score = s

print "max_score:", max_score
