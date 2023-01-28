from register import register_solution


def parse_input(filename):
    with open(filename) as f:
        line = f.readline().strip().split()
        return [int(x) for x in line]


class Node:
    def __init__(self):
        self.children = []
        self.metadata = []
        self.val = None

    def parse(self, nums, indent=0):
        num_children = nums[0]
        num_metadata = nums[1]
        print(" "*indent + "parsing node:", num_children, num_metadata)
        nums = nums[2:]

        for x in range(0, num_children):
            child = Node()
            nums = child.parse(nums, indent + 2)
            self.children.append(child)

        self.metadata = nums[:num_metadata]

        print(" "*indent + "finished node:", num_children, num_metadata, "metadata:", self.metadata)


        return nums[num_metadata:]

    def metadata_sum(self):
        self_sum = sum(self.metadata)
        children_sum = sum([x.metadata_sum() for x in self.children])
        # print("Node sum:", self_sum, "Children sum:", children_sum)
        return self_sum + children_sum

    def value(self):
        if self.val is None:
            if len(self.children) == 0:
                self.val = sum(self.metadata)
            else:
                self.val = 0
                for x in self.metadata:
                    idx = x-1
                    if idx in range(0, len(self.children)):
                        self.val += self.children[idx].value()
        return self.val


@register_solution(2018, 8, 1)
def part1(filename):
    nums = parse_input(filename)
    tree = Node()
    tree.parse(nums)
    print("part1:", tree.metadata_sum())

@register_solution(2018, 8, 2)
def part2(filename):
    nums = parse_input(filename)
    tree = Node()
    tree.parse(nums)
    print("part2:", tree.value())
