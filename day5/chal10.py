
def pairRepeating(word):
    for i in range(0, len(word)-1):
        pair = word[i] + word[i+1]
        remaining = word[:i]+ "#" + word[i+2:]
        if pair in remaining:
            print "###", pair, remaining
            return True
    return False

def repeatedSkip1(word):
    for i in range(0, len(word)-2):
        if word[i] == word[i+2]:
            print i, word[i]
            return True
    return False

# read in file
f = open("chal9_input.txt")

nice = 0
for line in f:
    word = line.strip()
    print word
    if pairRepeating(word) and repeatedSkip1(word):
        nice += 1

print "Nice words:", nice
