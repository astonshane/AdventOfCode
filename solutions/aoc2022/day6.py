from register import register_solution


def find_marker(line, look_ahead=4):
    for i in range(0, len(line)):
        marker = line[i:i + look_ahead]
        if len(set(marker)) == look_ahead:
            return i + look_ahead


assert(find_marker("mjqjpqmgbljsphdztnvjfqwrcgsmlb") == 7)
assert(find_marker("bvwbjplbgvbhsrlpgdmjqwftvncz") == 5)
assert(find_marker("nppdvjthqldpwncqszvftbrmjlhg") == 6)
assert(find_marker("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg") == 10)
assert(find_marker("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw") == 11)
assert(find_marker("mjqjpqmgbljsphdztnvjfqwrcgsmlb", 14) == 19)
assert(find_marker("bvwbjplbgvbhsrlpgdmjqwftvncz", 14) == 23)
assert(find_marker("nppdvjthqldpwncqszvftbrmjlhg", 14) == 23)
assert(find_marker("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 14) == 29)
assert(find_marker("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 14) == 26)


@register_solution(2022, 6, 1)
def part1(filename):
    with open(filename) as f:
        line = f.readline()
        print("Part1:", find_marker(line))


@register_solution(2022, 6, 2)
def part1(filename):
    with open(filename) as f:
        line = f.readline()
        print("Part2:", find_marker(line, 14))
