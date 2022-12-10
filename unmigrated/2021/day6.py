def iterate(days):
    with open("inputs/day6.txt") as f:
        input = [int(x) for x in f.readline().strip().split(",")]
        fish = {}
        for f in input:
            fish[f] = fish.get(f, 0) + 1

        for day in range(1, days+1):
            new_fish = {}
            for x in fish:
                if x == 0:
                    new_fish[6] = new_fish.get(6,0) + fish[x]
                    new_fish[8] = fish[x]
                else:
                    new_fish[x-1] = new_fish.get(x-1, 0) + fish[x]
            fish = new_fish

        fish_count = sum(fish.values())
        return fish_count

print("part1:", iterate(80))
print("part2:", iterate(256))
