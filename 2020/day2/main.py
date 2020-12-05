def part1():
    count = 0
    with open("input.txt") as f:
        for line in f:
            line = line.strip().split()

            [lower, upper] = [int(x) for x in line[0].split("-")]
            search = line[1][0]
            pwd = line[2]

            search_count = pwd.count(search)
            if search_count >= lower and search_count <= upper:
                count += 1
        print(count)

def part2():
    count = 0
    with open("input.txt") as f:
        for line in f:
            line = line.strip().split()

            [i, j] = [int(x)-1 for x in line[0].split("-")]
            search = line[1][0]
            pwd = line[2]
            
            a = pwd[i] == search
            b = pwd[j] == search
            if a != b:
                count += 1
                #print(line)


        print(count)


part1()
part2()