def captcha(s, offset=1):
    sum = 0
    for i in range(0, len(s)):
        j = (i+offset) % len(s)
        if s[i] == s[j]:
            sum += int(s[i])
    return sum

# test cases for part 1
assert captcha("1122") == 3
assert captcha("1111") == 4
assert captcha("1234") == 0
assert captcha("91212129") == 9

# test cases for part 2 (only difference is that the offset to the next item we want to inspect is input.length / 2 instead of 1)
assert captcha("1212", 2) == 6
assert captcha("1221", 2) == 0
assert captcha("123425", 3) == 4
assert captcha("123123", 3) == 12
assert captcha("12131415", 4) == 4

with open("inputs/day1.txt") as f:
    for line in f:
        line = line.strip()
        print("part1:", captcha(line))
        print("part2:", captcha(line, int(len(line)/2)))