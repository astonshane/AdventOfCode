def twist(l, i, length):
    # put the elements to be reversed into a stack
    stack = []
    j = i
    size = length
    while size > 0:
        stack.append(l[j])
        j = (j+1) % len(l)
        size -= 1
    
    #print(stack)
    # reverse it
    stack.reverse()
    #print(stack)

    # put it back
    j = i
    size = 0
    while size < length:
        l[j] = stack[size]
        j = (j+1) % len(l)
        size += 1

    #print(l)
    return l


def part1():
    with open("inputs/day10.txt") as f:
        line = f.readline().strip()
        lengths = [int(x) for x in line.split(",")]
        N = 256
        l = list(range(0, N))

        i = 0 # current pos
        skip = 0 # skip size

        for length in lengths:
            #print("##################")
            #print("length", length, "i", i)
            #print(l)

            l = twist(l, i, length)
            i = (i + length + skip) % len(l)
            skip += 1
        print("part1:", l[0] * l[1])

def part2():
    with open("inputs/day10.txt") as f:
        line = f.readline().strip()
        lengths = [ord(x) for x in line]
        lengths.extend([17,31,73,47,23])
        N = 256
        l = list(range(0, N))

        i = 0 # current pos
        skip = 0 # skip size

        for round in range(0, 64):
            for length in lengths:
                #print("##################")
                #print("length", length, "i", i)
                #print(l)

                l = twist(l, i, length)
                i = (i + length + skip) % len(l)
                skip += 1
        

        dense_hash = []

        for i in range(0, 16):
            output = l[i*16]
            for j in range(1, 16):
                x = i*16 + j
                output = output ^ l[x]
            dense_hash.append(output)
        print(dense_hash)

        final = ""
        for x in dense_hash:
            final += format(x, 'x')
        print(final, len(final))


part1()
part2()