import math

with open("inputs/day7.txt") as f:
    input = [int(x) for x in f.readline().strip().split(",")]

    start = min(input)
    end = max(input)
    min_fuel = math.inf

    for i in range(start, end+1):
        fuel = 0
        for x in input:
            fuel += abs(i-x)
        if fuel < min_fuel:
            min_fuel = fuel
    print("part1:", min_fuel)

fuel_usage = {0:0, 1:1}

def fuelUsage(x):
    if x not in fuel_usage:
        fuel_usage[x] = fuelUsage(x-1) + x
    return fuel_usage[x]


with open("inputs/day7.txt") as f:
    input = [int(x) for x in f.readline().strip().split(",")]

    start = min(input)
    end = max(input)

    min_fuel = math.inf

    # pre-populate the fuel-usage memoization otherwise we hit max-recursion depth
    for i in range(0, end):
        fuelUsage(i)

    for i in range(start, end+1):
        fuel = 0
        for x in input:
            fuel += fuelUsage(abs(i-x))
        if fuel < min_fuel:
            min_fuel = fuel
    print("part2:", min_fuel)