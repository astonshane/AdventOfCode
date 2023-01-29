from register import register_solution


def parse_input(filename):
    with open(filename) as f:
        line = f.readline().strip().split()
        return int(line[0]), int(line[-2])

# doubly-linked list
class Node:
    def __init__(self, number, before=None, after=None):
        self.number = number
        self.next = self
        self.prev = self

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return str(self.number)


def clockwise(node, num=1):
    for _ in range(0, num):
        node = num.next
    return node


def counter_clockwise(node, num=1):
    for _ in range(0, num):
        node = node.prev
    return node


def print_circle(current):
    node = current
    while node.number != 0:
        node = node.next

    while True:
        if node.number == current.number:
            print("(%d)" % node.number, end=' ')
        else:
            print(node.number, end=' ')
        node = node.next
        if node.number == 0:
            print("")
            break

def run(num_players, highest_marble):
    players = [0 for _ in range(0, num_players)]
    current = Node(0)
    # print_circle(current)

    player_idx = 0
    marble_number = 1

    while marble_number <= highest_marble:
        # print_circle(current)
        if marble_number % 23 == 0:
            node_to_remove = counter_clockwise(current, 7)
            current = node_to_remove.next
            node_to_remove.prev.next = current

            players[player_idx] += marble_number + node_to_remove.number
        else:
            one_ahead = current.next
            two_ahead = one_ahead.next
            new_node = Node(marble_number)

            one_ahead.next = new_node
            new_node.prev = one_ahead
            new_node.next = two_ahead
            two_ahead.prev = new_node

            current = new_node

        player_idx = (player_idx + 1) % len(players)
        marble_number += 1

    # print_circle(current)
    return max(players)


assert(run(9, 25) == 32)
assert(run(13, 7999) == 146373)
assert(run(17, 1104) == 2764)
assert(run(21, 6111) == 54718)
assert(run(30, 5807) == 37305)


@register_solution(2018, 9, 1)
def part1(filename):
    num_players, highest_marble = parse_input(filename)
    print(run(num_players, highest_marble))


@register_solution(2018, 9, 2)
def part2(filename):
    num_players, highest_marble = parse_input(filename)
    print(run(num_players, highest_marble*100))
