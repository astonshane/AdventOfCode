def checksum(spreadsheet):
    count = 0
    for line in spreadsheet:
        count += max(line) - min(line)
    return count

def lineChecksum(line):
    previous = []
    for x in line:
        for y in previous:
            if x % y == 0:
                return x / y
            elif y % x == 0:
                return y / x
        previous.append(x)


def checksum2(spreadsheet):
    count = 0
    for line in spreadsheet:
        count += lineChecksum(line)
    return int(count)


spreadsheet = []
with open("inputs/day2.txt") as f:
    for line in f:
        line = line.strip().split()
        line = [int(x) for x in line]
        spreadsheet.append(line)

print("part1:", checksum(spreadsheet))
print("part2:", checksum2(spreadsheet))

