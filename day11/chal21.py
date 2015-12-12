import sys


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


# ######################
if len(sys.argv) != 2:
    print "need a starting password"
    exit(1)

password = sys.argv[1]
print "original:   ", password
password = increment(password)  # we have to increment at least once
while True:
    print password
    if validPassword(password):
        break
    else:
        password = increment(password)

print "new:        ", password
