import md5
from sets import Set

SALT = "yjdafjpo"
PART2 = True
hashes = {}

def parseDigest(digest):
    resp = {
        'digest': digest,
        3: None,
        5: Set()
    }
    findTripple=True
    for i in range(0, len(digest)-2):
        if findTripple and digest[i]*3 == digest[i:i+3]:
            findTripple = False
            resp[3] = digest[i]*3

        if i+3 < len(digest) and i+4 < len(digest) and digest[i]*5 == digest[i:i+5]:
            resp[5].add(digest[i]*5)

    return resp

def hashIndex(index):
    if index not in hashes:
        m = md5.new()
        m.update(SALT + str(index))
        digest = m.hexdigest()

        if PART2:
            for i in range(0, 2016):
                m = md5.new()
                m.update(digest)
                digest = m.hexdigest()

        hashes[index] = parseDigest(digest)

index = -1
valid_keys = 0

while valid_keys < 64:
    index += 1
    hashIndex(index)
    if hashes[index][3] is not None:
        for i in range(1, 1001):
            hashIndex(index+i)
            if hashes[index][3][0]*5 in hashes[index+i][5]:
                valid_keys += 1
                print "%d found valid hash at index %d:" % (valid_keys, index), hashes[index]['digest']
                break


print "last index:", index
