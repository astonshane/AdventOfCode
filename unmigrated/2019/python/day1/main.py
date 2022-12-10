# fuel = low(mass / 3) - 2

def calcFuel(mass):
    fuel = int(mass / 3) - 2
    if fuel < 0:
        return 0
    return fuel + calcFuel(fuel)

assert calcFuel(14) == 2
assert calcFuel(1969) == 966
assert calcFuel(100756) == 50346

with open("input.txt") as f:
    total_fuel = 0
    for line in f:
        total_fuel += calcFuel(int(line))
    print total_fuel