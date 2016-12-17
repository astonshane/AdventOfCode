def step(a):
    b = a[::-1]

    resp = ''

    for c in b:
        if c == '1':
            resp += '0'
        else:
            resp += '1'
    resp = a + '0' + resp
    assert(len(resp) == len(a)*2+1)
    return resp

def expand(a, size):
    if len(a) >= size:
        return a[:size]
    return expand(step(a), size)

def checksum(inp):
    if len(inp) % 2 == 1:
        return inp

    a = ''
    for i in range(0, len(inp)-1, 2):
        if inp[i] == inp[i+1]:
            a += '1'
        else:
            a += '0'

    return checksum(a)

inp = '11011110011011101'
size = 35651584
exp = expand(inp, size)

chk = checksum(exp)
print chk
