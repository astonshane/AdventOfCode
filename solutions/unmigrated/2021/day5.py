PART2 = True

def printTestBoard(marks):
    for i in range(0, 10):
        for j in range(0, 10):
            print(marks.get((j, i), '.'), end="")
        print("")

with open("inputs/day5.txt") as f:

    marks = {}

    for line in f:
        line = line.strip().split(" -> ")
        line = [x.split(",") for x in line]
        line = [(int(x[0]), int(x[1])) for x in line]
        [a,b] = line

        if not PART2 and a[0] != b[0] and a[1] != b[1]:
            continue

        # vertical line
        if a[0] == b[0]:
            x = a[0]
            y1 = min(a[1], b[1])
            y2 = max(a[1], b[1])

            while y1 <= y2:
                marks[(x, y1)] = marks.get((x, y1), 0) + 1
                y1 += 1

        # horizontal line
        elif a[1] == b[1]:
            y = a[1]
            x1 = min(a[0], b[0])
            x2 = max(a[0], b[0])

            while x1 <= x2:
                marks[(x1, y)] = marks.get((x1, y), 0) + 1
                x1 += 1

        # diagonals
        else:
            xfactor = None
            yfactor = None

            if a[0] < b[0]:
                xfactor = 1
            else:
                xfactor = -1

            if a[1] < b[1]:
                yfactor = 1
            else:
                yfactor = -1


            while a != b:
                marks[a] = marks.get(a, 0) + 1
                a = (a[0] + xfactor, a[1] + yfactor)
            marks[b] = marks.get(b, 0) + 1

    #printTestBoard(marks)

    overlap = 0
    for key in marks:
        if marks[key] > 1:
            overlap += 1
    print("answer:", overlap)
