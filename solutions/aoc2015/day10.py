from register import register_solution

def run(val, iterations):
    cnt = 0
    newVal = ""

    for i in range(0, iterations):
        j = 0
        while j < len(val):
            cnt += 1
            if j + 1 >= len(val) or val[j] != val[j + 1]:
                newVal += str(cnt) + val[j]
                cnt = 0
            j += 1

        val = newVal
        newVal = ""
        cnt = 0

    print("length of final value:", len(val))


@register_solution(2015, 10, 1)
def part1(filename):
    with open(filename) as f:
        val = f.readline().strip()
        run(val, 40)


@register_solution(2015, 10, 2)
def part2(filename):
    with open(filename) as f:
        val = f.readline().strip()
        run(val, 50)
