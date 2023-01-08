from register import register_solution
import json


def countObj(obj, ignoreRed=False):
    if type(obj) is int:
        return obj
    elif type(obj) is list:
        count = 0
        for o in obj:
            count += countObj(o, ignoreRed)
        return count
    elif type(obj) is dict:
        if ignoreRed and "red" in obj.values():
            return 0
        count = 0
        for o in obj:
            if type(obj[o]) is int:
                count += obj[o]
            else:
                count += countObj(obj[o], ignoreRed)
        return count
    return 0

@register_solution(2015, 12, 1)
def part1(filename):
    with open(filename) as f:
        for line in f:
            obj = json.loads(line)
            print(countObj(obj))


@register_solution(2015, 12, 2)
def part2(filename):
    with open(filename) as f:
        for line in f:
            obj = json.loads(line)
            print(countObj(obj, ignoreRed=True))
