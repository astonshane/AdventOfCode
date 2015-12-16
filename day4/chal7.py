import md5

secret = "ckczppom"

m = md5.new()

m.update(secret)

i = 1
while(1):
    print i,
    m1 = m.copy()
    m1.update(str(i))
    hsh = m1.hexdigest()
    print hsh
    if hsh[:5] == "00000":
        print i
        break
    i += 1
