import binascii

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

def knotHash(key, rounds=1):
    lengths = [ord(x) for x in key]
    lengths.extend([17, 31, 73, 47, 23])
    l = list(range(0, 256)) # starting empty list
    
    i = 0 # current_pos
    skip = 0 # skip size
    for round in range(0, rounds):
        for length in lengths:
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

    final = ""
    #print(len(dense_hash))
    for x in dense_hash:
        tmp = format(x, 'x')
        if len(tmp) == 1:
            tmp = "0" + tmp
        final += tmp
        #print(final)
    #print(final, len(final))
    return final

def hashToBinaryString(hash):
    b = ""
    for x in hash:
        tmp = str(bin(int(x, 16))[2:].zfill(4))
        b += tmp
    return b

'''
1010
0000
1100
0010
0000
0001
0111
0000
'''



assert(knotHash("", 64) == "a2582a3a0e66e6e86e3812dcb672a272")
assert(knotHash("AoC 2017", 64) == "33efeb34ea91902bb2f59c9920caa6cd")
assert(knotHash("1,2,3", 64) == "3efbe78a8d82f29979031a4aa0b16a9d")
assert(knotHash("1,2,4", 64) == "63960835bcdc130f0b66d7ff4f6a5a8e")

assert(hashToBinaryString("a0c2017") == "1010000011000010000000010111")

def mark(disk, i, j, region):
    if i >= 0 and i < 128 and j >= 0 and j < 128:
        if disk[i][j] == "#":
            disk[i][j] = str(region)
            disk = mark(disk, i+1, j, region)
            disk = mark(disk, i-1, j, region)
            disk = mark(disk, i, j+1, region)
            disk = mark(disk, i, j-1, region)

    return disk

with open("inputs/day14.txt") as f:
    key = f.readline().strip()
    #print(key)

    used_count = 0

    disk = []

    for i in range(0,128):
        row = "%s-%d" % (key, i)
        #print(row)
        hash = knotHash(row, rounds=64)
        #print(hash, len(hash))

        b = hashToBinaryString(hash)
        #print(row, hash, b)

        used_count += b.count("1")

        disk.append(list(b.replace("1", '#').replace("0", '.')))
    
    print("part1:", used_count)

    regions = 0
    for i in range(0, 128):
        for j in range(0,128):
            if disk[i][j] == '#':
                regions += 1
                disk = mark(disk, i, j, regions)

    #for row in disk:
    #    print("".join(row))

    print("part2:", regions)



        
