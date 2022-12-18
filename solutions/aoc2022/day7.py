from register import register_solution
from pprint import pprint


class Unit:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "unimplemented"

    def get_size(self):
        return None


class File(Unit):
    def __init__(self, name, size):
        self.size = size
        super().__init__(name)

    def __str__(self):
        return "%s (file, size=%d)" % (self.name, self.size)

    def get_size(self):
        return self.size


class Directory(Unit):
    def __init__(self, name):
        self.contents = []
        self.size = None
        super().__init__(name)

    def __str__(self):
        return "%s (dir)" % self.name

    def get_size(self):
        if self.size is None:
            self.size = 0
            for x in self.contents:
                self.size += x.get_size()
        return self.size


def get_path(path, filesystem):
    if path is None:
        return None

    if len(path) == 0:
        return filesystem

    if path[0] not in filesystem:
        filesystem[path[0]] = {}

    return get_path(path[1:], filesystem[path[0]])


all_dir_sizes = []


def calculate_sizes(filesystem):
    size = 0
    for key in filesystem:
        val = filesystem[key]
        if type(val) == int:
            size += val
        else:
            size += calculate_sizes(val)
    all_dir_sizes.append(size)
    return size


@register_solution(2022, 7, 1)
@register_solution(2022, 7, 2)
def part1(filename):

    filesystem = {}

    with open(filename) as f:
        path = None
        for line in f:
            #print("current path:", path)
            pwd = get_path(path, filesystem)
            line = line.strip().split()
            #print(line)
            if line[0] == '$':
                # new command
                if line[1] == "cd":
                    if line[2] == "/":
                        path = ["/"]
                        filesystem["/"] = {}
                    elif line[2] == "..":
                        path.pop()
                    else:
                        path.append(line[2])

                elif line[1] == "ls":
                    pass
                else:
                    print("unknown command!")
            else:
                # ls
                if line[0] == 'dir':
                    pass
                else:
                    get_path(path, filesystem)[line[1]] = int(line[0])
        pprint(filesystem, indent=2, width=1)

    current_used = calculate_sizes(filesystem)
    # print(current_used)
    # print(all_dir_sizes)
    answer = sum([x for x in all_dir_sizes if x < 100000])
    print("Part1:", answer)

    all_dir_sizes.sort()

    unused = 70000000 - current_used
    # print("unused", unused)

    for x in all_dir_sizes:
        if unused + x > 30000000:
            print("Part2:", x)
            break



