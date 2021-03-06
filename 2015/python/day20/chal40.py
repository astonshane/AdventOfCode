import math


def divisors(x):
    lst = set()
    for i in range(1, min(50, int(math.floor(math.pow(x, 0.5)))) + 1):
        if x % i == 0:
            lst.add(x/i)
    lst.add(x)
    return lst

goal = 36000000

house = 1
gifts = 0
while(gifts < goal):
    divs = divisors(house)
    gifts = sum(divs)*11
    print house, gifts, goal - gifts
    house += 1
