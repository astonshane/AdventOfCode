from register import register_solution
import copy

MAX_TEASPOONS = 100

def get_ingredients(filename):
    ingredients = {}
    with open(filename) as f:
        for line in f:
            line = line.strip().split(":")
            ingredient = line[0]
            properties = line[1].split(',')
            props = {}
            for prop in properties:
                prop = prop.strip().split(' ')
                props[prop[0]] = int(prop[1])

            ingredients[ingredient] = props
    return ingredients


def assignValues(assignments, remainingKeys, assigned):
    permutations = []
    toAssign = remainingKeys[0]
    remainingKeys.remove(toAssign)
    if len(remainingKeys) == 0:
        assignments[toAssign] = MAX_TEASPOONS - assigned
        permutations.append(assignments)
    else:
        for i in range(0, MAX_TEASPOONS - assigned + 1):
            newAssignments = copy.copy(assignments)
            newAssignments[toAssign] = i
            permutations += assignValues(newAssignments, copy.copy(remainingKeys), assigned + i)
    return permutations


@register_solution(2015, 15, 1)
def part1(filename):
    def score(assignment, catagories, ingredients):
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

    ingredients = get_ingredients(filename)

    keys = list(ingredients.keys())
    permutations = assignValues({}, keys, 0)

    max_score = None

    catagories = list(ingredients[list(ingredients.keys())[0]].keys())
    catagories.remove('calories')

    for p in permutations:
        s = score(p, catagories, ingredients)
        if max_score is None or s > max_score:
            max_score = s

    print("max_score:", max_score)




@register_solution(2015, 15, 2)
def part2(filename):
    def score(assignment, catagories, ingredients):
        score = 1
        calories = 0
        print
        assignment,
        for ingredient in assignment:
            calories += ingredients[ingredient]['calories'] * assignment[ingredient]
        print
        calories
        if calories != 500:
            return None

        for cat in catagories:
            cat_score = 0
            for ingredient in assignment:
                cat_score += ingredients[ingredient][cat] * assignment[ingredient]
            if cat_score < 0:
                score *= 0
            else:
                score *= cat_score

        return score

    ingredients = get_ingredients(filename)
    keys = list(ingredients.keys())
    permutations = assignValues({}, keys, 0)
    max_score = None

    catagories = list(ingredients[list(ingredients.keys())[0]].keys())
    catagories.remove('calories')

    for p in permutations:
        s = score(p, catagories, ingredients)
        if s is not None and (max_score is None or s > max_score):
            max_score = s

    print("max_score:", max_score)
