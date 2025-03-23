from register import register_solution
from operator import mul
from functools import reduce

class Robot:
    def __init__(self, line, width, height):
        line = line.strip().split(" ")
        [x, y] = [int(x) for x in line[0].split("=")[1].split(",")]
        [vx, vy] = [int(x) for x in line[1].split("=")[1].split(",")]

        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy

        self.width = width
        self.height = height

    def move(self):
        self.x = (self.x + self.width + self.vx) % self.width
        self.y = (self.y + self.height + self.vy) % self.height
    
    def __str__(self) -> str:
        return f"Robot({self.x}, {self.y})"
    
    def __repr__(self) -> str:
        return self.__str__()
    
def parseInput(filename, width, height):
    with open(filename) as f:
        robots = [Robot(line, width, height) for line in f]
        return robots
    
def findCounts(robots):
    counts = {}
    for robot in robots:
        if (robot.x, robot.y) not in counts:
            counts[(robot.x, robot.y)] = 0
        counts[(robot.x, robot.y)] += 1
    return counts

def printBoard(robots, width, height):
    counts = findCounts(robots)

    for y in range(0, height):
        row = ""
        for x in range(0, width):
            row += str(counts.get((x, y), '.'))
        print(row)

def score(robots, width, height):
    quadrants = [0, 0, 0, 0]
    for robot in robots:
        if robot.x < width//2 and robot.y < height//2:
            quadrants[0] += 1
        elif robot.x > width//2 and robot.y < height//2:
            quadrants[1] += 1
        elif robot.x < width//2 and robot.y > height//2:
            quadrants[2] += 1
        elif robot.x > width//2 and robot.y > height//2:
            quadrants[3] += 1
    print(quadrants)
    return reduce(mul, quadrants)
    

@register_solution(2024, 14, 1)
def part1(filename):
   # (width, height) = (11, 7)
    (width, height) = (101, 103)
    seconds = 100

    robots = parseInput(filename, width, height)
    # print(robots)
    # printBoard(robots, width, height)

    for i in range(0, seconds):
        for robot in robots:
            robot.move()

    # print(robots)
    # printBoard(robots, width, height)
    print(score(robots, width, height))
        


@register_solution(2024, 14, 2)
def part2(filename):
    (width, height) = (101, 103)
    seconds = 100
    robots = parseInput(filename, width, height)
    seconds = 0
    while True:
        seconds += 1
        for robot in robots:
            robot.move()

        if len(findCounts(robots).keys()) == len(robots):
            printBoard(robots, width, height)
            print(f"seconds: {seconds}")
            x = input("continue? ")
            if x == 'n':
                break
