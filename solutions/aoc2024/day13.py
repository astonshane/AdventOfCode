from register import register_solution
from queue import PriorityQueue

def parseButtonLine(line):
    line = line.split(": ")[1].split(',')
    return [int(x.split('+')[1]) for x in line]

def parsePrizeLine(line):
    line = line.split(": ")[1].split(',')
    return [int(x.split('=')[1]) for x in line]

def parseInput(filename):
    with open(filename) as f:
        machines = []
        machine = []
        for line in f:
            line = line.strip()
            if "Button" in line:
                machine.append(parseButtonLine(line))
            elif "Prize" in line:
                machine.append(parsePrizeLine(line))
                machines.append(machine)
                machine = []
        return machines

# BFS - too slow
# def solveMachine(a, b, prize):
#     print(f"machine {a}, {b}, prize {prize}")
#     pq = PriorityQueue()
#     # current_tokens, x, y
#     pq.put((0, 0, 0))
#     checked = set()


#     while not pq.empty():
#         val = pq.get()
#         (tokens, x, y) = val
#         # print(f"checking {tokens}, {x}, {y}")
#         if x == prize[0] and y == prize[1]:
#             print(f"found solution: {tokens}")
#             return tokens
        
#         a_press = (tokens + 3, x + a[0], y + a[1])
#         if x + a[0] <= prize[0] and y + a[1] <= prize[1] and a_press not in checked:
#             checked.add(a_press)
#             pq.put(a_press)
        
#         b_press = (tokens + 1, x + b[0], y + b[1])
#         if x + b[0] <= prize[0] and y + b[1] <= prize[1] and b_press not in checked:
#             checked.add(b_press)
#             pq.put(b_press)

#     print("no solution")
#     return 0

def solveMachine(a, b, prize):
    # print(f"machine {a}, {b}, prize {prize}")
    # A = 0 # how many times we've pressed A
    # B = 0 # how many times we've pressed B

    xA = a[0] # how much we move in x when we press A
    yA = a[1] # how much we move in y when we press A
    xB = b[0] # how much we move in x when we press B
    yB = b[1] # how much we move in y when we press B

    xP = prize[0] # x coordinate of the prize
    yP = prize[1] # y coordinate of the prize

    # if you start with these two equations:
    # A * xA + B * xB = xP
    # A * yA + B * yB = yP
    # then solve both for A:
    # A = (xP - B * xB) / xA
    # A = (yP - B * yB) / yA
    # then set them equal to each other and solve for B:
    B = (xA * yP - yA * xP) / (xA * yB - yA * xB)

    # then plug B back into the first equation to solve for A:
    A = (xP - B * xB) / xA

    # if both A and B are integers we have a solution
    if A == int(A) and B == int(B):
        A = int(A)
        B = int(B)
        # print(f"found solution: A: {A} B: {B} ({A*3 + B})")
        return A*3 + B

    # print("no solution")
    return 0

@register_solution(2024, 13, 1)
def part1(filename):
    machines = parseInput(filename)
    print(f"total: {sum([solveMachine(a, b, prize) for (a, b, prize) in machines])}")
    # for (a, b, prize) in machines:
    #     solveMachine(a, b, prize)


@register_solution(2024, 13, 2)
def part2(filename):
    machines = parseInput(filename)
    print(f"total: {sum([solveMachine(a, b, [prize[0] + 10000000000000, prize[1] + 10000000000000]) for (a, b, prize) in machines])}")
