import re

def part1():
    f = open("inputs/day4.txt")

    sector_sum = 0

    for line in f:
        m = re.search('(.+)-(\d+)\[(.+)\]', line.strip())
        (encrypted_name, sector_id, given_checksum) = m.groups()
        name = ''.join(encrypted_name.split('-'))

        letter_map = {}
        count_map = {}

        for c in name:
            if c in letter_map:
                letter_map[c] += 1
            else:
                letter_map[c] = 1
        for key in letter_map:
            if letter_map[key] in count_map:
                count_map[letter_map[key]].append(key)
            else:
                count_map[letter_map[key]] = [key]

        count_keys = count_map.keys()
        count_keys.sort(reverse=True)

        checksum = ''
        for key in count_keys:
            count_map[key].sort()
            for c in count_map[key]:
                checksum += c
                if len(checksum) == 5:
                    break
            if len(checksum) == 5:
                break

        if checksum == given_checksum:
            sector_sum += int(sector_id)

    print "(part1):", sector_sum

def convert(letter, sector_id):
    if letter == '-':
        return ' '
    return chr(((ord(letter)-97+sector_id) % 26) + 97)

def part2():
    f = open("inputs/day4.txt")
    solution_id = None
    for line in f:
        m = re.search('(.+)-(\d+)\[(.+)\]', line.strip())
        (encrypted_name, sector_id, given_checksum) = m.groups()
        #name = ''.join(encrypted_name.split('-'))
        decrypted_name = ''

        for c in encrypted_name:
            decrypted_name += convert(c, int(sector_id))
        print decrypted_name, sector_id
        if "north" in decrypted_name:
            solution_id = sector_id

    print "(part2):", solution_id

part1()
part2()
