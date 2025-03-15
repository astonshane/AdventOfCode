from register import register_solution
from itertools import permutations

def validateLine(line, rules):
    problems = set()
    for x in line:
        if x in problems:
            return False
        
        problems = problems.union(rules.get(x, set()))
    return True

def process(filename):
    with open(filename) as f:
        rules = {}
        for line in f:
            line = line.strip()
            if line == "":
                break
            [x, y] = [int(x) for x in line.split('|')]
            if y not in rules:
                rules[y] = set()
            rules[y].add(x)
    
        correct_lines = []
        incorrect_lines = []

        for line in f:
            line = line.strip()
            line = [int(x) for x in line.split(',')]

            if validateLine(line, rules):
                correct_lines.append(line)
            else:
                incorrect_lines.append(line)

        return rules, correct_lines, incorrect_lines


@register_solution(2024, 5, 1)
def part1(filename):
    _, correct_lines, _ = process(filename)
    total = 0
    for line in correct_lines:
        middle_index = len(line) // 2
        total += line[middle_index]
    print(total)

def correctLine(line, rules):
    #print("correcting line", line)
    # lazyyyyy and inefficient
    corrected_line = []
    # for number x in line:
    # if any of rules[x] is already in corrected_line:
    #    put x as right before the minimum of their inedexes
    # else:
    #    put x at the end

    for x in line:
        problems = rules.get(x, set())
        problem_indexes = [corrected_line.index(y) for y in problems if y in corrected_line]
        if len(problem_indexes) > 0:
            min_index = min(problem_indexes)
            corrected_line.insert(min_index, x)
        else:
            corrected_line.append(x)

    #print(corrected_line)
    return corrected_line

@register_solution(2024, 5, 2)
def part2(filename):
    rules, _, incorrect_lines = process(filename)
    total = 0
    #print("total incorrect lines", len(incorrect_lines))
    for line in incorrect_lines:
        corrected_line = correctLine(line, rules)
        middle_index = len(corrected_line) // 2
        total += corrected_line[middle_index]
    print(total)
