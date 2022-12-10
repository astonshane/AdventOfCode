import sys

if len(sys.argv) != 3:
    print "need an input value and # of iterations"
    exit(1)

val = sys.argv[1]
iterations = int(sys.argv[2])
print val, iterations

cnt = 0
newVal = ""

for i in range(0, iterations):
    # print val
    j = 0
    while(j < len(val)):
        cnt += 1
        if j+1 >= len(val) or val[j] != val[j+1]:
            newVal += str(cnt) + val[j]
            cnt = 0
        j += 1

    val = newVal
    newVal = ""
    cnt = 0


print "\n\nfinal value:", val
print "length of final value:", len(val)
