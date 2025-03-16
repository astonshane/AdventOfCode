from register import register_solution

def parseInput(filename):
    with open(filename) as f:
        equations = []
        for line in f:
            line = line.strip().split(':')
            goal = int(line[0])
            numbers = [int(x) for x in line[1].strip().split(' ')]
            equations.append((goal, numbers))
        return equations
    
def solveEquation(goal, remaining_numbers, current_value=None, part2=False):
    # print(f"  Goal: {goal} Remaining: {remaining_numbers} Current: {current_value}")
    # check win condition
    if len(remaining_numbers) == 0:
        return current_value == goal
    
    # base case
    if current_value is None:
        return solveEquation(goal, remaining_numbers[1:], remaining_numbers[0], part2=part2)
    
    # recursive cases
    # try adding the next number
    if solveEquation(goal, remaining_numbers[1:], current_value + remaining_numbers[0], part2=part2):
        return True
    # try multiplying the next number
    if solveEquation(goal, remaining_numbers[1:], current_value * remaining_numbers[0], part2=part2):
        return True
    
    # try using the combination operator
    if part2:
        # 15 || 6 => 156
        next_value = int(str(current_value) + str(remaining_numbers[0]))
        if solveEquation(goal, remaining_numbers[1:], next_value, part2=part2):
            return True
    
    return False

@register_solution(2024, 7, 1)
def part1(filename):
    equations = parseInput(filename)
    print(sum(goal for (goal, numbers) in equations if solveEquation(goal, numbers)))
    # for (goal, numbers) in equations:
    #     print(f"Goal: {goal} Numbers: {numbers}")
    #     print(solveEquation(goal, numbers))
        

@register_solution(2024, 7, 2)
def part2(filename):
    equations = parseInput(filename)
    print(sum(goal for (goal, numbers) in equations if solveEquation(goal, numbers, part2=True)))
    # for (goal, numbers) in equations:
    #     print(f"Goal: {goal} Numbers: {numbers}")
    #     print(solveEquation(goal, numbers, part2=True))
