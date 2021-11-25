def serialize(memory):
    return ''.join([str(x) for x in memory])

def findLargestIndex(memory):
    index = 0
    for i in range(1, len(memory)):
        if memory[i] > memory[index]:
            index = i
    return index

def redistribute(memory):
    index = findLargestIndex(memory)
    blocks = memory[index]
    memory[index] = 0
    while blocks > 0:
        index = (index + 1) % len(memory)
        memory[index] += 1
        blocks -= 1

memory = None
with open("inputs/day6.txt") as f:
    memory = f.readline().strip().split()
    memory = [int(x) for x in memory]
print(memory)

# past_states = set() # set is more performant for part1 but for part2 we'll use a simple list
past_states = []

serialized = serialize(memory)
steps = 0
while serialized not in past_states:
    steps += 1
    past_states.append(serialized)
    redistribute(memory)
    serialized = serialize(memory)

print(memory)
print("part1:", steps)

previous = past_states.index(serialized)
print("part2:", len(past_states) - previous)