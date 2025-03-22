from register import register_solution

def parseInput(filename):
    with open(filename) as f:
        line = f.readline().strip().split()
        return [int(x) for x in line]

mem = {}

def process(stone, blinks) -> int:
    # print(f"processing ({stone},{blinks})")
    if blinks == 0:
        return 1
    
    if (stone, blinks) in mem:
        return mem[(stone, blinks)]
    
    val = None
    if stone == 0:
        val = process(1, blinks - 1)
    elif len(str(stone)) % 2 == 0:
        stone_str = str(stone)
        first_half = int(stone_str[:len(stone_str)//2])
        second_half = int(stone_str[len(stone_str)//2:])
        val = process(first_half, blinks - 1) + process(second_half, blinks - 1)
    else:
        val = process(2024*stone, blinks - 1)
    
    # print(f"memoizing ({stone},{blinks}) as {val}")
    mem[(stone, blinks)] = val
    return val

def solve(filename, blinks):
    stones = parseInput(filename)
    print(stones)
    length = sum([process(stone, blinks) for stone in stones])
    print(f"length after {blinks} blinks is {length}")

@register_solution(2024, 11, 1)
def part1(filename):
    solve(filename, 25)

@register_solution(2024, 11, 2)
def part2(filename):
   solve(filename, 75)
