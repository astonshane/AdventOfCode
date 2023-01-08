def spin(programs, size):
    x = programs[-size:]
    y = programs[:-size]
    x.extend(y)
    return x
assert(spin(["a","b","c","d","e"], 1) == ["e", "a","b","c","d"])

def exchange(programs, p1, p2):
    tmp = programs[p1]
    programs[p1] = programs[p2]
    programs[p2] = tmp
    return programs
assert(exchange(["a","b","c","d","e"], 3, 4) == ["a","b","c","e","d"])

def partner(programs, p1, p2):
    i1 = programs.index(p1)
    i2 = programs.index(p2)
    return exchange(programs, i1, i2)
assert(partner(["a","b","c","d","e"], "a", "c") == ["c","b","a","d","e"])

with open("inputs/day16.txt") as f:
    instructions = f.readline().strip().split(",")
    #print(instructions)

    START_SIZE = 16

    base_case = ''.join([chr(97+x) for x in range(0, START_SIZE)])
    programs = [chr(97+x) for x in range(0, START_SIZE)]
    #print(programs)

    known_states = [base_case]

    for iteration in range(0, 1000000000):
        for instruction in instructions:
            i = instruction[0]
            if i == 's':
                programs = spin(programs, int(instruction[1:]))
            elif i == 'x':
                [a,b] = [int(x) for x in instruction[1:].split("/")]
                programs = exchange(programs, a, b)
            elif i == 'p':
                [a,b] = instruction[1:].split("/")
                programs = partner(programs, a, b)
            else:
                print("unknown instruction!", instruction)

        end_state = ''.join(programs)
        if iteration == 0:
            print("part1:", end_state)
        
        if end_state == base_case:
            break
        known_states.append(end_state)

    #print("cycle size?", len(known_states))

    i = 1000000000 % len(known_states)
    print("part2", known_states[i])

            
       
    
