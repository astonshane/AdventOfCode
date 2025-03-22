from register import register_solution
import re

def getInput(filename):
    with open(filename) as f:
        return f.readline().strip()
    
def expand(input):
    expanded = []
    id = 0
    is_file = True
    for c in input:
        if is_file:
            expanded.extend([id] * int(c))
            id += 1
            is_file = False
        else:
            expanded.extend(['.'] * int(c))
            is_file = True
    return expanded, id-1

def compress(input):
    forward_iterator = 0
    reverse_iterator = len(input) - 1

    while True:
        while input[forward_iterator] != '.':
            forward_iterator += 1
            if forward_iterator >= len(input):
                break

        if set(input[forward_iterator:]) == {'.'}:
            break

        while input[reverse_iterator] == '.':
            reverse_iterator -= 1
            if reverse_iterator < 0:
                break
        
        if forward_iterator >= len(input) or reverse_iterator < 0:
            break

        # print(f"before: {''.join(input)}")
        # print(f"Swapping Forward: {forward_iterator} {input[forward_iterator]} Reverse: {reverse_iterator} {input[reverse_iterator]}")
        input[forward_iterator] = input[reverse_iterator]
        input[reverse_iterator] = '.'
        # print(f"after:  {''.join(input)}")
        # print(set(input[forward_iterator:]))
    return input

def checksum(input):
    checksum = 0
    for i in range(0, len(input)):
        # print(f"{i}: {input[i]}")
        if input[i] == '.':
            continue
        checksum += i * input[i]
    return checksum

@register_solution(2024, 9, 1)
def part1(filename):
    input = getInput(filename)
    print(input)

    expanded, _ = expand(input)    
    print(expanded)

    compressed = compress(expanded)
    print(compressed)

    print(checksum(compressed))


def compress2(input, max_id):
    # print(input, max_id)

    for x in range(max_id, -1, -1):
        count = input.count(x)
        first_index = input.index(x)
        #print(x, count, first_index)

        for i in range(0, first_index):
            if input[i] == '.' and len(set(input[i:i+count])) == 1:
                #print(f"found empty space starting at {i}")
                for y in range(0, count):
                    input[i+y] = x
                    input[first_index+y] = '.'
                break

    return input


@register_solution(2024, 9, 2)
def part2(filename):
    input = getInput(filename)
    print(input)

    expanded, max_id = expand(input)    
    print(expanded)

    compressed = compress2(expanded, max_id)
    print(compressed)
    #print(''.join([str(x) for x in compressed]))

    print(checksum(compressed))
