from register import register_solution
import re

def increment(last_value):
    inter = last_value * 252533
    next_value = inter % 33554393
    return next_value


@register_solution(2015, 25, 1)
@register_solution(2015, 25, 2)
def part1(filename):
    with open(filename) as f:
        column = row = None
        for line in f:
            matchObj = re.match(
                r'To continue, please consult the code grid in the manual.  Enter the code at row (\d*), column (\d*).',
                line, re.M | re.I)

            row = int(matchObj.group(1)) - 1
            column = int(matchObj.group(2)) - 1

        value = None
        paper = []
        start = 20151125
        paper.append([start])
        last_value = start
        while value is None:
            paper.append([])
            last_i = len(paper) - 1
            for i in range(last_i, -1, -1):
                paper[i].append(increment(last_value))
                j = len(paper[i]) - 1
                last_value = paper[i][-1]
                if row == i and column == j:
                    value = last_value
            # printPaper(paper)

        print("Value =", value)

