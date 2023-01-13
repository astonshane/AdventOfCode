from register import register_solution
from hashlib import md5
hashes = {}


def parseDigest(digest):
    resp = {
        'digest': digest,
        3: None,
        5: set()
    }
    findTripple = True
    for i in range(0, len(digest)-2):
        if findTripple and digest[i]*3 == digest[i:i+3]:
            findTripple = False
            resp[3] = digest[i]*3

        if i+3 < len(digest) and i+4 < len(digest) and digest[i]*5 == digest[i:i+5]:
            resp[5].add(digest[i]*5)

    return resp


def hashIndex(index, part2):
    SALT = "yjdafjpo"
    if index not in hashes:
        m = md5((SALT + str(index)).encode())
        digest = m.hexdigest()

        if part2:
            for i in range(0, 2016):
                m = md5(digest.encode())
                digest = m.hexdigest()

        hashes[index] = parseDigest(digest)


def run(part2=False):
    index = -1
    valid_keys = 0

    while valid_keys < 64:
        index += 1
        hashIndex(index, part2)
        if hashes[index][3] is not None:
            for i in range(1, 1001):
                hashIndex(index + i, part2)
                if hashes[index][3][0] * 5 in hashes[index + i][5]:
                    valid_keys += 1
                    print("%d found valid hash at index %d:" % (valid_keys, index), hashes[index]['digest'])
                    break

    print("last index:", index)


@register_solution(2016, 14, 1)
def part1(filename):
    run(False)


@register_solution(2016, 14, 2)
def part2(filename):
    run(True)
