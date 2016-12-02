f = open("chal15_input.txt")

total_length = 0
total_unescaped_length = 0

for line in f:
    full = line[:-1]
    full_length = len(full)

    print full

    final_length = full_length
    for i in range(0, len(full)):
        if full[i] == '\\' or full[i] == '\"':
            final_length += 1



    total_length += full_length
    total_unescaped_length += final_length + 2

print "Total Length:", total_length
print "Total un-Escaped Length:", total_unescaped_length
print "Difference:", total_unescaped_length - total_length
