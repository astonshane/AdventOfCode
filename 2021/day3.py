import statistics

with open("inputs/day3.txt") as f:
    flat = [[x] for x in f.readline().strip()]
    #print(flat)
    for line in f:
        line = line.strip()
        for i in range(0, len(line)):
            flat[i].append(line[i])
    #print(flat)

    gamma = ""
    epsilon = ""

    for x in flat:
        most_common = statistics.mode(x)
        gamma += most_common
        epsilon += '0' if most_common == '1' else '1'
    #print(gamma, epsilon)
    gamma = int(gamma, 2)
    epsilon = int(epsilon, 2)
    #print(gamma, epsilon)
    power_consumption = gamma * epsilon
    print("part1:", power_consumption)


# determine the most common value (0 or 1). If 0 and 1 are equally common, keep values with a 1 in the position being considered.
def mostCommon(l):
    zeros = l.count('0')
    ones = l.count('1')

    if ones >= zeros:
        return '1'
    return '0'

# determine the least common value (0 or 1). If 0 and 1 are equally common, keep values with a 0 in the position being considered.
def leastCommon(l):
    zeros = l.count('0')
    ones = l.count('1')

    if zeros <= ones:
        return '0'
    return '1'

def reduce(lines, index, criteria):
    if len(lines) == 1:
        return lines[0]

    column = [x[index] for x in lines]
    factor = criteria(column)
    
    new_lines = []
    for x in lines:
        if x[index] == factor:
            new_lines.append(x)

    return reduce(new_lines, index+1, criteria)

with open("inputs/day3.txt") as f:
    lines = []
    for line in f:
        lines.append(line.strip())

    ox = lines
    co2 = lines.copy()

    #print(ox)


    ox_rating = reduce(ox, 0, mostCommon)
    co2_rating = reduce(co2, 0, leastCommon)
    #print(co2)

    #print(ox_rating, co2_rating)

    ox_rating = int(ox_rating, 2)
    co2_rating = int(co2_rating, 2)

    #print(ox_rating, co2_rating)

    life_support_rating = ox_rating * co2_rating
    print("part2:", life_support_rating)