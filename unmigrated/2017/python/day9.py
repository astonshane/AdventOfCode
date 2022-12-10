with open("inputs/day9.txt") as f:
    for line in f:
        line = line.strip()

        total_score = 0
        score = 0
        index = 0
        garbage_time = False
        garbage_count = 0

        while index < len(line):
            if line[index] == "!":
                index += 2
                continue

            if garbage_time:
                if line[index] == ">":
                    garbage_time = False
                else:
                    garbage_count += 1
            else:
                if line[index] == '{':
                    score += 1
                    total_score += score
                elif line[index] == "}":
                    score -= 1
                elif line[index] == "<":
                    garbage_time = True
            
            index += 1

        print("part1:", total_score)
        print("part2:", garbage_count)