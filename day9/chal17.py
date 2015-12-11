import copy

distances = {}


def findRoute(city, toVisit, currentLength):
    if len(toVisit) == 0:
        return currentLength
    dists = []
    for c in toVisit:
        newToVisit = copy.copy(toVisit)
        newToVisit.remove(c)
        dists.append(findRoute(c, newToVisit, currentLength + distances[city][c]))

    return min(dists)

f = open("chal17_input.txt")

# read in the file
for line in f:
    s = line.strip().split(' ')

    city1 = s[0]
    city2 = s[2]

    dist = s[-1]

    if city1 not in distances:
        distances[city1] = {}
    distances[city1][city2] = int(dist)

    if city2 not in distances:
        distances[city2] = {}
    distances[city2][city1] = int(dist)

print distances

min_dist = None

for city in distances:
    # pick a city to start at
    print "Starting at:", city
    all_cities = distances.keys()
    all_cities.remove(city)
    dist = findRoute(city, all_cities, 0)
    if min_dist is None or dist < min_dist:
        min_dist = dist

print "minimum distance:", min_dist
