from register import register_solution
import copy


def get_distances(filename):
    distances = {}
    with open(filename) as f:
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
    return distances

def findRoute(city, toVisit, currentLength, distances, f=min):
    if len(toVisit) == 0:
        return currentLength
    dists = []
    for c in toVisit:
        newToVisit = copy.copy(toVisit)
        newToVisit.remove(c)
        dists.append(findRoute(c, newToVisit, currentLength + distances[city][c], distances, f))

    return f(dists)

@register_solution(2015, 9, 1)
def part1(filename):
    distances = get_distances(filename)
    min_dist = None

    for city in distances:
        # pick a city to start at
        all_cities = set(distances.keys())
        all_cities.remove(city)
        dist = findRoute(city, all_cities, 0, distances, f=min)
        if min_dist is None or dist < min_dist:
            min_dist = dist

    print("minimum distance:", min_dist)


@register_solution(2015, 9, 2)
def part2(filename):
    distances = get_distances(filename)
    max_dist = None

    for city in distances:
        # pick a city to start at
        all_cities = set(distances.keys())
        all_cities.remove(city)
        dist = findRoute(city, all_cities, 0, distances, f=max)
        if max_dist is None or dist > max_dist:
            max_dist = dist

    print("max distance:", max_dist)
