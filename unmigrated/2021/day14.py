from pprint import pprint
import math

def factorize(base):
    pairs = {}

    for i in range(0, len(base)-1):
        pair = base[i:i+2]
        pairs[pair] = pairs.get(pair, 0) + 1
    return pairs


def iterate(base, rules, steps):
    pairs = factorize(base)
    for i in range(0, steps):
        new_pairs = {}
        for x in pairs:
            if x in rules:
                a = x[0]
                b = x[1]
                c = rules[x]
                p1 = a+c
                p2 = c+b
                new_pairs[p1] = new_pairs.get(p1, 0) + pairs[x]
                new_pairs[p2] = new_pairs.get(p2, 0) + pairs[x]
            else:
                new_pairs[x] = new_pairs.get(x, 0) + pairs[x]
        pairs = new_pairs

    return pairs

# What do you get if you take the quantity of the most common element and subtract the quantity of the least common element?
def score(pairs):
    counts = {}

    def inc(i, val):
        counts[i] = counts.get(i, 0) + val

    for x in pairs:
        inc(x[0], pairs[x])
        inc(x[1], pairs[x])

    for x in counts:
        counts[x] = math.ceil(counts[x] / 2)

    #pprint(counts)

    most_common = max(counts.values())
    least_common = min(counts.values())

    return most_common - least_common




with open("inputs/day14.txt") as f:
    base = f.readline().strip()
    f.readline()

    rules = {}
    for line in f:
        line = line.strip().split(" -> ")
        rules[line[0]] = line[1]

    #assert(iterate("NNCB", rules, 1) == factorize("NCNBCHB"))
    #assert(iterate("NNCB", rules, 2) == factorize("NBCCNBBBCBHCB"))
    #assert(iterate("NNCB", rules, 3) == factorize("NBBBCNCCNBBNBNBBCHBHHBCHB"))
    #assert(iterate("NNCB", rules, 4) == factorize("NBBNBNBBCCNBCNCCNBBNBBNBBBNBBNBBCBHCBHHNHCBBCBHCB"))

    print("part1", score(iterate(base, rules, 10)))   
    print("part2", score(iterate(base, rules, 40)))        
    