f = open("chal3_input.txt")
length = 0
for line in f:
    dimensions = sorted([int(x) for x in line.strip().split('x')])
    sublength = 2*dimensions[0] + 2*dimensions[1]
    sublength += dimensions[0]*dimensions[1]*dimensions[2]
    print sublength
    length += sublength
print "Total length:", length
