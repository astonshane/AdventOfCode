from register import register_solution
from hashlib import md5


def find_n_leading_zeros(secret, n):
    m = md5(secret.encode())
    search = '0' * n

    i = 1
    while True:
        m1 = m.copy()
        m1.update(str(i).encode())
        hsh = m1.hexdigest()
        if hsh[:n] == search:
            print(i)
            break
        i += 1

@register_solution(2015, 4, 1)
def part1(filename):
    find_n_leading_zeros("ckczppom", 5)


@register_solution(2015, 4, 2)
def part2(filename):
    find_n_leading_zeros("ckczppom", 6)
