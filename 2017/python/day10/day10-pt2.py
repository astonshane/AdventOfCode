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
    for rnd in range(0, 64):
       for length in lengths:
           numbers = reverseSubset(numbers, index, length)
           index += length + skip_size
           skip_size += 1
    return numbers
     

def createDenseHash(sparse_hash):
    dense_hash = []
    for i in range(0, 16):
        block = sparse_hash[0+i*16:16 + 16*i]
        val = None
        for x in block:
            if val is None:
                val = x
            else:
                val = val ^ x
        dense_hash.append(val)
    return dense_hash

def denseHashToHex(dense_hash):
    h = ""
    for x in dense_hash:
        h += hex(x)[2:]
    return h
        

with open("input.txt") as f:
    lengths = [ord(x) for x in f.readline().strip()]
    lengths.extend([17, 31, 73, 47, 23])
    numbers = [x for x in range(0, 256)]

    sparse_hash = knotHash(numbers, lengths)
    dense_hash = createDenseHash(numbers)
    hex_hash = denseHashToHex(dense_hash)

    print hex_hash
