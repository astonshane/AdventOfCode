def reverseSubset(numbers, start, length):
    for i in range(0, length/2):
        front = (start + i) % len(numbers)
        back = (start + length - 1 - i) % len(numbers)
        
        f = numbers[front]
        b = numbers[back]
        numbers[front] = b
        numbers[back] = f
    return numbers

def knotHash(numbers, lengths):
    index = 0
    skip_size = 0
    for length in lengths:
        print "#####################"
        print index, numbers, length
        numbers = reverseSubset(numbers, index, length)
        index += length + skip_size
        skip_size += 1
    print numbers
    return numbers[0] * numbers[1]

with open("input.txt") as f:
    lengths = [int(x) for x in f.readline().strip().split(",")]
    numbers = [x for x in range(0, 256)]

    print "numbers:", numbers
    print "lengths:", lengths

    print "KnotHash(): %d" % knotHash(numbers, lengths)