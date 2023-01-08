from register import register_solution

def splitPassword(password):
    p = []
    for c in password:
        p.append(c)
    return p


def combinePassword(password):
    p = ""
    for c in password:
        p += c
    return p


def increment(password):
    password = splitPassword(password)
    i = len(password)-1
    while True:
        if password[i] != 'z':
            password[i] = chr(ord(password[i])+1)
            break
        else:
            password[i] = 'a'
            i -= 1
    return combinePassword(password)


def threeStraight(password):
    for i in range(0, len(password) - 2):
        o = ord(password[i])
        if o + 1 == ord(password[i+1]) and o + 2 == ord(password[i+2]):
            return True
    return False


def noForbidden(password):
    return 'i' not in password and 'o' not in password and 'l' not in password


def twoPairs(password):
    foundOne = False
    for i in range(0, len(password) - 1):
        if password[i] == password[i+1]:
            if foundOne:
                return True
            else:
                password[i] = '|'
                password[i+1] = '|'
                foundOne = True
    return False


def validPassword(password):
    password = splitPassword(password)
    return threeStraight(password) and noForbidden(password) and twoPairs(password)


def newPassword(password):
    password = increment(password)
    while not validPassword(password):
        password = increment(password)
    return password


@register_solution(2015, 11, 1)
def part1(filename):
    with open(filename) as f:
        starting_password = f.readline().strip()
        print(newPassword(starting_password))


@register_solution(2015, 11, 2)
def part2(filename):
    with open(filename) as f:
        starting_password = f.readline().strip()
        print(newPassword(newPassword(starting_password)))
