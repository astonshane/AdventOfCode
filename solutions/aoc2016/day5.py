from register import register_solution
from hashlib import md5


@register_solution(2016, 5, 1)
def part1(filename):
    input = "ojvtpuvg"
    password = ""
    count = 0

    while len(password) != 8:
        m = md5((input + str(count)).encode())
        digest = m.hexdigest()

        if digest[:5] == "00000":
            password += digest[5]
            # print(password)
        count += 1

    print(password)


@register_solution(2016, 5, 2)
def part2(filename):
    input = "ojvtpuvg"
    password = [None] * 8
    count = 0

    while None in password:
        m = md5((input + str(count)).encode())
        digest = m.hexdigest()

        if digest[:5] == "00000":
            if digest[5] in [chr(i) for i in range(ord('0'), ord('8'))] and password[int(digest[5])] is None:
                password[int(digest[5])] = digest[6]
                # print(password)
        count += 1

    print(''.join(password))
