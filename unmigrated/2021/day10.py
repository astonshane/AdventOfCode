char_map = {
    "(": ")",
    "[": "]",
    "{": "}",
    "<": ">"
}

corrupt_points = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137
}

incomplete_points = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4
}

def scoreCompletion(chunk):
    score = 0
    for x in chunk:
        score = score*5 + incomplete_points[x]
    
    return score

assert(scoreCompletion("])}>") == 294)

def isCorrupt(chunk):
    keys = char_map.keys()

    stack = []
    
    for x in chunk:
        if x in keys:
            stack.append(x)
        else:
            if len(stack) == 0:
                return x
            y = stack.pop()
            if x != char_map[y]:
                return x

    return stack


assert(isCorrupt("(]") == "]") # corrupt
assert(isCorrupt("{()()()>") == ">") # corrupt
assert(isCorrupt("([])") == []) # valid
assert(isCorrupt("([") == ["(", "["]) # incomplete

with open("inputs/day10.txt") as f:
    corrupt_score = 0
    incomplete_scores = []
    for line in f:
        line = line.strip()
        val= isCorrupt(line)
        if type(val) == str: # complete
            corrupt_score += corrupt_points[val]
        else: # incomplete
            val.reverse()
            completion = [char_map[x] for x in val]
            score = scoreCompletion(completion)
            incomplete_scores.append(score)
    print("part1:", corrupt_score)
    incomplete_scores.sort()
    print("part2:", incomplete_scores[len(incomplete_scores) // 2])
