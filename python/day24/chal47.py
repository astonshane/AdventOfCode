import sys
import itertools


def product(group):
    prod = 1
    for i in group:
        prod *= i
    return prod

# ######################
if len(sys.argv) != 2:
    print "need an input file"
    exit(1)

f = open(sys.argv[1])

s = 0
nums = set()
weight = None
min_size = None
min_qe = None

for line in f:
    num = int(line.strip())
    s += num
    nums.add(num)

weight = s/3

perms = itertools.combinations(nums, 1)
for i in range(1, len(nums)-1):
    combos = itertools.combinations(nums, i)
    for group1 in combos:
        group1 = set(group1)
        remaining = nums - group1
        if (min_size is not None and len(group1) > min_size) or sum(group1) != weight:
            continue
        qe = product(group1)
        if min_qe is not None and qe > min_qe:
            continue
        for j in range(1, len(nums)-i):
            combos2 = itertools.combinations(remaining, j)
            for group2 in combos2:
                group2 = set(group2)
                if sum(group2) != weight:
                    continue
                if min_size is None or len(group1) < min_size or qe < min_qe:
                    min_size = len(group1)
                    min_qe = qe
                group3 = remaining - group2
                # print group1, group2, group3, qe
    if min_size is not None:
        break

print "minimum quantum entanglement:", min_qe
