import sys
import json


def countObj(obj):

    if type(obj) is int:
        return obj
    elif type(obj) is list:
        count = 0
        for o in obj:
            count += countObj(o)
        return count
    elif type(obj) is dict:
        if "red" in obj.values():
            return 0
        count = 0
        for o in obj:
            if type(obj[o]) is int:
                count += obj[o]
            else:
                count += countObj(obj[o])
        return count
    return 0


# ######################
if len(sys.argv) != 2:
    print "need an input file"
    exit(1)

f = open(sys.argv[1])

for line in f:
    obj = json.loads(line)
    print obj,
    print countObj(obj)
