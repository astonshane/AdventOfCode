from register import register_solution


@register_solution(2015, 8, 1)
def part1(filename):
    with open(filename) as f:
        total_length = 0
        total_escaped_length = 0
        for line in f:
            full = line[:-1]
            full_length = len(full)

            # print(full)

            # remove the beginning / end quotes
            partial = full[1:-1]
            partial_length = len(partial)

            i = 0
            while i < len(partial):
                if partial[i] == '\\':
                    if i + 1 < len(partial) and partial[i + 1] == 'x':
                        partial_length -= 3
                        i += 3
                    else:
                        # print("hit")
                        partial_length -= 1
                        i += 2
                else:
                    i += 1

            # print full, full_length, partial_length

            total_length += full_length
            total_escaped_length += partial_length

        print("Total Length:", total_length)
        print("Total Escaped Length:", total_escaped_length)
        print("Difference:", total_length - total_escaped_length)


@register_solution(2015, 8, 2)
def part2(filename):
    with open(filename) as f:
        total_length = 0
        total_unescaped_length = 0

        for line in f:
            full = line[:-1]
            full_length = len(full)

            final_length = full_length
            for i in range(0, len(full)):
                if full[i] == '\\' or full[i] == '\"':
                    final_length += 1

            total_length += full_length
            total_unescaped_length += final_length + 2

        print("Total Length:", total_length)
        print("Total un-Escaped Length:", total_unescaped_length)
        print("Difference:", total_unescaped_length - total_length)
