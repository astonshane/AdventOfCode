import math

def hexStrToBinStr(hexstr):
    bin = ""
    for c in hexstr:
        integer = int(c, 16)
        bin += format(integer, '0>4b')
    return bin


def parsePacket(bits, verbose=False, depth=0):
    total_length = 0
    if verbose:
        print("\t"*depth, "bits:", bits, len(bits))

    version = int(bits[0:3], 2)
    if verbose:
        print("\t"*depth, "version:", version)

    type_id = int(bits[3:6], 2)
    if verbose:
        print("\t"*depth, "type_id:", type_id)

    total_length += 6

    if type_id == 4:
        # literal value
        index = 6
        binstr = ""
        while True:
            stop = bits[index] == '0'
            binstr += bits[index+1:index+5]
            #print(binstr)
            index += 5
            total_length += 5
            if stop:
                break
        val = int(binstr, 2)
        if verbose:
            print("\t"*depth, "VAL:", val)

        # return value: remaining bits, packet length, value, version
        return bits[index:], total_length, val, version
    else: # all other types are operators
        values = []
        version_sum = version
        length_type_id = bits[6]
        total_length += 1
        if verbose:
            print("\t"*depth, "length_type_id:", length_type_id)

        count = 0
        

        if length_type_id == '0':
            # next 15 bits are a number that represents the total length in bits of the sub-packets contained by this packet
            max_packet_length = int(bits[7:7+15], 2)
            if verbose:
                print("\t"*depth, "max_packet_length:", max_packet_length)
            bits = bits[7+15:]
            total_length += 15

            contained_length = 0

            while contained_length < max_packet_length:
                x = parsePacket(bits, verbose, depth+1)
                if verbose:
                    print("\t"*depth, "return value:", x)
                (bits, length, value, version) = x
                values.append(value)
                version_sum += version
                count += 1
                contained_length += length
                total_length += length
                if verbose:
                    print("\t"*depth,"contained_length:", contained_length)
        else:
            # next 11 bits are a number that represents the number of sub-packets immediaetly conained by this pakcet
            max_packet_count = int(bits[7:7+11], 2)
            if verbose:
                print("\t"*depth, "max_packet_count:", max_packet_count)
            bits = bits[7+11:]
            total_length += 11

            while count < max_packet_count:
                x = parsePacket(bits, verbose, depth+1)
                if verbose:
                    print("\t"*depth, "return value:", x)
                (bits, length, value, version) = x
                values.append(value)
                version_sum += version
                count += 1
                total_length += length
                if verbose:
                    print("\t"*depth,"count:", count)
        
        val = None

        if type_id == 0:
            val = sum(values)
        elif type_id == 1:
            val = math.prod(values)
        elif type_id == 2:
            val = min(values)
        elif type_id == 3:
            val = max(values)
        elif type_id == 5:
            val = int(values[0] > values[1])
        elif type_id == 6:
            val = int(values[0] < values[1])
        elif type_id == 7:
            val = int(values[0] == values[1])

        return bits, total_length, val, version_sum

_, _, _, version_sum = parsePacket(hexStrToBinStr("38006F45291200"), verbose=False)
assert(version_sum == 9)

_, _, _, version_sum = parsePacket(hexStrToBinStr("EE00D40C823060"), verbose=False)
assert(version_sum == 14)

_, _, _, version_sum = parsePacket(hexStrToBinStr("8A004A801A8002F478"), verbose=False)
assert(version_sum == 16)

_, _, _, version_sum = parsePacket(hexStrToBinStr("620080001611562C8802118E34"), verbose=False)
assert(version_sum == 12)

_, _, _, version_sum = parsePacket(hexStrToBinStr("C0015000016115A2E0802F182340"), verbose=False)
assert(version_sum == 23)

_, _, _, version_sum = parsePacket(hexStrToBinStr("A0016C880162017C3686B18A3D4780"), verbose=False)
assert(version_sum == 31)

_, _, value, _ = parsePacket(hexStrToBinStr("C200B40A82"), verbose=False)
assert(value == 3)

_, _, value, _ = parsePacket(hexStrToBinStr("04005AC33890"), verbose=False)
assert(value == 54)

_, _, value, _ = parsePacket(hexStrToBinStr("9C0141080250320F1802104A08"), verbose=False)
assert(value == 1)

with open("inputs/day16.txt") as f:
    start = f.readline().strip()
    print("start:", start)
    bits = hexStrToBinStr(start)
    x = parsePacket(bits)
    #print(x)
    (_,_,part2, part1) = x
    print("part1:", part1)
    print("part2:", part2)