# needs at least 3 vowels
def vowelCount(word):
    count = 0
    for letter in word:
        if letter in ['a', 'e', 'i', 'o', 'u']:
            count += 1
    return count


# at least one repeated letter
def repeated(word):
    for i in range(0, len(word)-1):
        if word[i] == word[i+1]:
            return True
    return False


def contains(word, sub):
    return sub in word


# does not contain the strings ab, cd, pq, or xy
def containsStrings(word):
    return contains(word, "ab") or contains(word, "cd") or contains(word, "pq") or contains(word, "xy")


# read in file
f = open("chal9_input.txt")

nice = 0
for line in f:
    word = line.strip()
    print word

    # needs at least 3 vowels
    a = vowelCount(word) >= 3
    # at least one repeated letter
    b = repeated(word)
    # does not contain the strings ab, cd, pq, or xy
    c = not containsStrings(word)
    print a, b, c

    if a and b and c:
        nice += 1

print "Nice words:", nice
