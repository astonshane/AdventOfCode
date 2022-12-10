f = open("chal3_input.txt")
area = 0
for line in f:
    dimensions = [int(x) for x in line.strip().split('x')]
    a = dimensions[0]*dimensions[1]
    b = dimensions[0]*dimensions[2]
    c = dimensions[1]*dimensions[2]
    slack = min([a,b,c])
    subarea = 2*a + 2*b + 2*c + slack
    print subarea
    area += subarea
print "Total Area:", area
