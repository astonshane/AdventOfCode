def score(line):
    i = 0
    score = 0
    garbage = False
    scoreMultiplyer = 0
    garbageCharacters = 0

    while i < len(line):
        character = line[i]

        if garbage and character == "!":
            i += 1
        elif garbage and character == ">":
            garbage = False
        elif garbage:
            garbageCharacters += 1
        elif not garbage and character == "<":
            garbage = True
        elif character == "{":
            scoreMultiplyer += 1
            score += scoreMultiplyer
        elif character == "}":
            scoreMultiplyer -= 1
        
       
        i += 1
    return score, garbageCharacters


with open("input.txt") as f:
    for line in f:
        line = line.strip()
        score, garbageCount = score(line)
        print "%s : %d : %s" % (line, score, garbageCount)