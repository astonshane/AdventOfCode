from itertools import permutations

with open("inputs/day8.txt") as f:
    # counting just 1,4,7,8 from output
    count = 0
    for line in f:
        line = line.strip().split(" | ")
        [signals , outputs] = [x.split() for x in line]
        #print(signals, outputs)

        for o in outputs:
            # #1
            if len(o) == 2:
                count += 1
            # 4
            elif len(o) == 4:
                count += 1            
            # 7
            elif len(o) == 3:
                count += 1
            # 8
            elif len(o) == 7:
                count += 1
    print("part1:", count)
        

digits = {
    0: set(["a", "b", "c", "e", "f", "g"]),
    1: set(["c", "f"]),
    2: set(["a", "c", "d", "e", "g"]),
    3: set(["a", "c", "d", "f", "g"]),
    4: set(["b", "c", "d", "f"]),
    5: set(["a", "b", "d", "f", "g"]),
    6: set(["a", "b", "d", "e", "f", "g"]),
    7: set(["a", "c", "f"]),
    8: set(["a", "b", "c", "d", "e", "f", "g"]),
    9: set(["a", "b", "c", "d", "f", "g"])
}
digit_list = ["a", "b", "c", "d", "e", "f", "g"]
digit_perms = list(permutations(digit_list))

def translate(signal, translation_map):
    tmp = set()
    for s in signal:
        tmp.add(translation_map[s])

    return tmp

def getMapping(signal):
    for x in digits:
        if digits[x] == signal:
            return x
    return None


# awful horrible brute force solution
with open("inputs/day8.txt") as f:
    # counting just 1,4,7,8 from output
    count = 0

    for line in f:
        line = line.strip().split(" | ")
        [signals , outputs] = [x.split() for x in line]
        #print(signals, outputs)

        # for each possible permuation of mappings, translate each signal and if all match then you can do the outputs
        for perm in digit_perms:
            #print("trying permutation:", perm)
            translation_map = {}
            for i in range(0, 7):
                translation_map[perm[i]] = digit_list[i]
            
            valid = True
            for signal in signals:
                s = translate(signal, translation_map)
                d = getMapping(s)
                #print("signal %s translates to:" % signal, s, d)
                if d is None:
                    valid = False
                    break
            
            if not valid:
                continue
            #print("valid mapping!", perm)

            output_str = ""
            for x in outputs:
                output_str += str(getMapping(translate(x, translation_map)))
            #print(output_str)
            count += int(output_str)
            break

    print("part2:", count)