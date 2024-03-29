from register import register_solution


def parseCmd(cmd, source, values, todo):
    if values.get(source) is not None:
        return
    if len(cmd) == 1:
        value = cmd[0]
        if value.isdigit():
            values[source] = int(value)
        elif value in values:
            values[source] = values[value]
        else:
            todo.append([source, cmd])
    elif len(cmd) == 2 and cmd[0] == "NOT":
        value = cmd[1]
        if value.isdigit():
            values[source] = ~int(value)
        elif value in values:
            values[source] = ~values[value]
        else:
            todo.append([source, cmd])
    elif len(cmd) == 3 and cmd[1] == "AND":
        v1 = None
        v2 = None

        if cmd[0].isdigit():
            v1 = int(cmd[0])
        elif cmd[0] in values:
            v1 = values[cmd[0]]

        if cmd[2].isdigit():
            v2 = int(cmd[2])
        elif cmd[2] in values:
            v2 = values[cmd[2]]

        if v1 is None or v2 is None:
            todo.append([source, cmd])
        else:
            values[source] = v1 & v2
    elif len(cmd) == 3 and cmd[1] == "OR":
        v1 = None
        v2 = None

        if cmd[0].isdigit():
            v1 = int(cmd[0])
        elif cmd[0] in values:
            v1 = values[cmd[0]]

        if cmd[2].isdigit():
            v2 = int(cmd[2])
        elif cmd[2] in values:
            v2 = values[cmd[2]]

        if v1 is None or v2 is None:
            todo.append([source, cmd])
        else:
            values[source] = v1 | v2

    elif len(cmd) == 3 and cmd[1] == "LSHIFT":
        v1 = None
        v2 = None

        if cmd[0].isdigit():
            v1 = int(cmd[0])
        elif cmd[0] in values:
            v1 = values[cmd[0]]

        if cmd[2].isdigit():
            v2 = int(cmd[2])
        elif cmd[2] in values:
            v2 = values[cmd[2]]

        if v1 is None or v2 is None:
            todo.append([source, cmd])
        else:
            values[source] = v1 << v2
    elif len(cmd) == 3 and cmd[1] == "RSHIFT":
        v1 = None
        v2 = None

        if cmd[0].isdigit():
            v1 = int(cmd[0])
        elif cmd[0] in values:
            v1 = values[cmd[0]]

        if cmd[2].isdigit():
            v2 = int(cmd[2])
        elif cmd[2] in values:
            v2 = values[cmd[2]]

        if v1 is None or v2 is None:
            todo.append([source, cmd])
        else:
            values[source] = v1 >> v2

    else:
        todo.append([source, cmd])


def run(filename, values={}):
    todo = []

    with open(filename) as f:
        # initial parsing
        for line in f:
            s = line.strip().split("->")
            source = s[1].strip()
            cmd = s[0].split()
            # print(source, cmd)
            parseCmd(cmd, source, values, todo)

        while len(todo) > 0:
            new_todo = todo
            todo = []
            for item in new_todo:
                parseCmd(item[1], item[0], values, todo)

        return values['a']

@register_solution(2015, 7, 1)
def part1(filename):
    print(run(filename))


@register_solution(2015, 7, 2)
def part2(filename):
    values = {}
    values['b'] = run(filename)
    print(run(filename, values))
