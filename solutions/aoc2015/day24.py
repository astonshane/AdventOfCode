from register import register_solution
import itertools


def product(group):
    prod = 1
    for i in group:
        prod *= i
    return prod


def parse_input(filename, groups):
    nums = set()
    s = 0
    with open(filename) as f:
        for line in f:
            num = int(line.strip())
            s += num
            nums.add(num)
    return nums, s / groups


@register_solution(2015, 24, 1)
def part1(filename):
    nums, weight = parse_input(filename, 3)
    min_size = None
    min_qe = None

    for i in range(1, len(nums) - 1):
        combos = itertools.combinations(nums, i)
        for group1 in combos:
            group1 = set(group1)
            remaining = nums - group1
            if (min_size is not None and len(group1) > min_size) or sum(group1) != weight:
                continue
            qe = product(group1)
            if min_qe is not None and qe > min_qe:
                continue
            for j in range(1, len(nums) - i):
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

    print("minimum quantum entanglement:", min_qe)


@register_solution(2015, 24, 2)
def part2(filename):
    nums, weight = parse_input(filename, 4)
    min_size = None
    min_qe = None

    for i in range(1, len(nums) - 1):
        combos = itertools.combinations(nums, i)
        for group1 in combos:
            group1 = set(group1)
            remaining = nums - group1
            if (min_size is not None and len(group1) > min_size) or sum(group1) != weight:
                continue
            qe = product(group1)
            if min_qe is not None and qe >= min_qe:
                continue
            for j in range(1, len(nums) - i):
                if min_size == len(group1):
                    break
                combos2 = itertools.combinations(remaining, j)
                for group2 in combos2:
                    if min_size == len(group1):
                        break
                    group2 = set(group2)
                    if sum(group2) != weight:
                        continue
                    remaining2 = remaining - group2
                    for k in range(1, len(nums) - i - j):
                        if min_size == len(group1):
                            break
                        combos3 = itertools.combinations(remaining2, k)
                        for group3 in combos3:
                            group3 = set(group3)
                            if sum(group3) != weight:
                                continue
                            if min_size is None or len(group1) < min_size or qe < min_qe:
                                min_size = len(group1)
                                min_qe = qe
                            group4 = remaining2 - group3
        if min_size is not None:
            break

    print("minimum quantum entanglement:", min_qe)
