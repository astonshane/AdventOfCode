from register import register_solution


@register_solution(2015, 5, 1)
def part1(filename):
    # needs at least 3 vowels
    def vowelCount(word):
        count = 0
        for letter in word:
            if letter in ['a', 'e', 'i', 'o', 'u']:
                count += 1
        return count

    # at least one repeated letter
    def repeated(word):
        for i in range(0, len(word) - 1):
            if word[i] == word[i + 1]:
                return True
        return False

    def contains(word, sub):
        return sub in word

    # does not contain the strings ab, cd, pq, or xy
    def containsStrings(word):
        return contains(word, "ab") or contains(word, "cd") or contains(word, "pq") or contains(word, "xy")

    with open(filename) as f:
        nice = 0
        for line in f:
            word = line.strip()
            # print(word)

            # needs at least 3 vowels
            a = vowelCount(word) >= 3
            # at least one repeated letter
            b = repeated(word)
            # does not contain the strings ab, cd, pq, or xy
            c = not containsStrings(word)
            # print(a, b, c)

            if a and b and c:
                nice += 1

        print("Nice words:", nice)


@register_solution(2015, 5, 2)
def part2(filename):
    def pairRepeating(word):
        for i in range(0, len(word) - 1):
            pair = word[i] + word[i + 1]
            remaining = word[:i] + "#" + word[i + 2:]
            if pair in remaining:
                print
                "###", pair, remaining
                return True
        return False

    def repeatedSkip1(word):
        for i in range(0, len(word) - 2):
            if word[i] == word[i + 2]:
                print
                i, word[i]
                return True
        return False

    with open(filename) as f:
        nice = 0
        for line in f:
            word = line.strip()
            if pairRepeating(word) and repeatedSkip1(word):
                nice += 1

        print("Nice words:", nice)