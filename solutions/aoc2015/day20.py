from register import register_solution
import math

goal = 36000000

@register_solution(2015, 20, 1)
def part1(filename):
    def divisors(x):
        lst = set()
        for i in range(1, int(math.floor(math.pow(x, 0.5))) + 1):
            if x % i == 0:
                lst.add(i)
                lst.add(x / i)
        lst.add(x)
        return lst

    house = 1
    gifts = 0
    while gifts < goal:
        divs = divisors(house)
        gifts = sum(divs) * 10
        # print(house, gifts, goal - gifts)
        house += 1
    print(house-1)


@register_solution(2015, 20, 2)
def part2(filename):
    def divisors(x):
        lst = set()
        for i in range(1, min(50, int(math.floor(math.pow(x, 0.5)))) + 1):
            if x % i == 0:
                lst.add(x / i)
        lst.add(x)
        return lst

    house = 1
    gifts = 0
    while gifts < goal:
        divs = divisors(house)
        gifts = sum(divs) * 11
        # print(house, gifts, goal - gifts)
        house += 1
    print(house-1)
