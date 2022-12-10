with open("inputs/day17.txt") as f:
    line = f.readline().strip().split()

    TARGETx = line[-2]
    TARGETx = [int(i) for i in TARGETx.split('=')[1].strip(',').split('..')]

    TARGETy = line[-1]
    TARGETy = [int(i) for i in TARGETy.split('=')[1].strip(',').split('..')]


def inTargetArea(x, y):
    #if x in range(TARGETx[0], TARGETx[1]+1):
    #    print("in x!")
    return x in range(TARGETx[0], TARGETx[1]+1) and y in range(TARGETy[0], TARGETy[1]+1)

def fire(vx, vy):
    #print("FIRE! w/velocity %d,%d" % (vx, vy))
    x = 0
    y = 0
    ymax=0

    step = 0
    while True:
        #print("step: %d pos: (%d,%d) velocity: (%d,%d)" % (step, x, y, vx, vy))
        if inTargetArea(x,y):
            return True, ymax

        # this condition probably needs work...
        if y < TARGETy[1]:
            return False, ymax

        x += vx
        y += vy
        ymax = max(y, ymax)

        if vx > 0:
            vx -= 1
        elif vx < 0:
            vx += 1

        vy -= 1
        step += 1


# only works with the test data
'''hit, tmax = fire(7,2)
assert(hit == True)
assert(tmax == 3)

hit, tmax = fire(6,3)
assert(hit == True)
assert(tmax == 6)

hit, tmax = fire(9,0)
assert(hit == True)
assert(tmax == 0)

hit, tmax = fire(17,-4)
assert(hit == False)'''


supermax = 0
for x in range(-100, 1000):
    for y in range(0, 100):
        hit, tmax = fire(x,y)
        if hit:
            supermax = max(supermax, tmax)

print("part1:", supermax)