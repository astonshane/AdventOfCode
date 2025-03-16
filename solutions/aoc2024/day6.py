from register import register_solution
from enum import Enum
from copy import deepcopy
from multiprocessing import Pool

class Direction(Enum):
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3

class Guard:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.visited = set()
        self.visited.add((x, y))        
        self.direction = Direction.NORTH
        self.visited_with_direction = set()
        self.visited_with_direction.add((x, y, self.direction.value))

    def turn(self):
        self.direction = Direction((self.direction.value + 1) % 4)

    def nextCoords(self):
        next_x = None
        next_y = None
        if self.direction == Direction.NORTH:
            next_x = self.x
            next_y = self.y-1
        elif self.direction == Direction.EAST:
            next_x = self.x+1
            next_y = self.y
        elif self.direction == Direction.SOUTH:
            next_x = self.x
            next_y = self.y+1
        elif self.direction == Direction.WEST:
            next_x = self.x-1
            next_y = self.y

        if (next_x, next_y, self.direction.value) in self.visited_with_direction:
            #print("Loop detected!")
            return None

        return (next_x, next_y)
        
    def move(self, x, y):
        self.x = x
        self.y = y
        self.visited.add((x, y))
        self.visited_with_direction.add((x, y, self.direction.value))

    def directionCharacter(self):
        if self.direction == Direction.NORTH:
            return '^'
        elif self.direction == Direction.EAST:
            return '>'
        elif self.direction == Direction.SOUTH:
            return 'v'
        elif self.direction == Direction.WEST:
            return '<'

    def __str__(self) -> str:
        return f"Guard at ({self.x}, {self.y}) facing {self.direction.name} with {len(self.visited)} visited"

def parseBoard(filename):
    with open(filename) as f:
        board = []
        for line in f:
            line = line.strip()
            if line == "":
                break
            line = list(line)
            board.append(line)
        return board
    
def printBoard(board, guard):
    board[guard.y][guard.x] = guard.directionCharacter()
    print("######### board #########")
    for line in board:
        print(''.join(line))
    print("#########################")
    board[guard.y][guard.x] = '.'

@register_solution(2024, 6, 1)
def part1(filename):
    board = parseBoard(filename)
    guard = None
    # find the starting point
    for y in range(0, len(board)):
        if '^' in board[y]:
            x = board[y].index('^')
            board[y][x] = '.'
            guard = Guard(x, y)
            break
    
    while True:
        #print(guard)
        (next_x, next_y) = guard.nextCoords()
        # check if next coords are valid
        if next_y < 0 or next_y >= len(board) or next_x < 0 or next_x >= len(board[0]):
            #print("Next Step Out of bounds!")
            break
        # check if next coords are blocked
        if board[next_y][next_x] == '#':
            #printBoard(board, guard)
            guard.turn()
            continue
        guard.move(next_x, next_y)

    print(guard)

def hasLoop(board, guard):
    while True:
        nextCoords = guard.nextCoords()
        if nextCoords is None:
            return 1
        (next_x, next_y) = nextCoords
        # check if next coords are valid
        if next_y < 0 or next_y >= len(board) or next_x < 0 or next_x >= len(board[0]):
            #print("Next Step Out of bounds!")
            break
        # check if next coords are blocked
        if board[next_y][next_x] == '#':
            #printBoard(board, guard)
            guard.turn()
            continue
        guard.move(next_x, next_y)
    return 0

@register_solution(2024, 6, 2)
def part2(filename):
    board = parseBoard(filename)
    guard = None
    # find the starting point
    for y in range(0, len(board)):
        if '^' in board[y]:
            x = board[y].index('^')
            board[y][x] = '.'
            guard = Guard(x, y)
            break

    print(guard)
    if guard is None:
        return

    with Pool(10) as p:
        results = []
        for y in range(0, len(board)):
            for x in range(0, len(board[0])):
                if x == guard.x and y == guard.y:
                    continue
                board_copy = deepcopy(board)
                board_copy[y][x] = '#'
                result = p.apply_async(hasLoop, [board_copy, Guard(guard.x, guard.y)])
                #print(result)
                results.append(result)

        print(sum([result.get() for result in results]))