import numpy

rules = {}
starting_pattern = [".#.", "..#", "###"]
starting_pattern = [x.split() for x in starting_pattern]

def print_grid(grid):
    print('=' * (len(grid) + 4))
    print('\n'.join([''.join(x) for x in grid]))
    print('=' * (len(grid) + 4))


print("base")
print_grid(starting_pattern)
print("flip ud")
print_grid(numpy.flipud(starting_pattern))
print("flip lr")
print_grid(numpy.fliplr(starting_pattern))
print("rot90")
print_grid(numpy.rot90(starting_pattern, k=1).tolist())
#print_grid(numpy.rot90(starting_pattern, k=2))
#print_grid(numpy.rot90(starting_pattern, k=3))


with open("inputs/test/day21.txt") as f:
    for line in f:
        line = line.strip().split(" => ")
        #print(line)