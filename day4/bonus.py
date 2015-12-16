import md5
import sys

# ######################
if len(sys.argv) != 2:
    print "need a check length"
    exit(1)
length = int(sys.argv[1])
print '0'*length

secret = "ckczppom"
out = "coins.txt"
f = open(out, 'w')
f.close()

m = md5.new()

m.update(secret)

i = 1
while(1):
    m1 = m.copy()
    m1.update(str(i))
    hsh = m1.hexdigest()
    if hsh[:length] == "0"*length:
        print i, hsh
        f = open(out, 'a')
        f.write("%d %s\n" % (i, hsh))
        f.close()
    i += 1
