class Layer:
    def __init__(self, range):
        self.range = range
        #self.l = ['']*range
        #self.l[0] = "S"
        self.s_index = 0
        self.forward = True

        self.save_state = (0, True)
    
    def advance(self):
        # assuems that all ranges are >= 2
        if self.forward:
            self.s_index += 1

            # we've reached the end, the next stage should send us back up the list
            if self.s_index == (self.range-1):
                self.forward = False
        else:
            # we're back at the begining, start going back down again
            self.s_index -= 1
            if self.s_index == 0:
                self.forward = True

    def collision(self):
        return self.s_index == 0

    def save(self):
        self.save_state = (self.s_index, self.forward)

    def restore(self):
        self.s_index = self.save_state[0]
        self.forward = self.save_state[1]

class EmptyLayer:
    def collision(self):
        return False


with open("inputs/day13.txt") as f:
    firewall = {}
    for line in f:
        [layer, depth] = line.strip().split(": ")
        firewall[int(layer)] = Layer(int(depth))
    end = max(firewall.keys())

    severity = 0

    for picosecond in range(0, end+1):
        layer = firewall.get(picosecond, EmptyLayer())
        if layer.collision():
            severity += picosecond*layer.range
        
        for layer in firewall:
            firewall[layer].advance()
    
    print("part1:", severity)


def printFirewall(firewall):
    for layer in firewall:
        print("%d,%d" % (layer, firewall[layer].s_index), end="\t")
    print("")


# this takes foreverrrrrrrrrrrr to run but will eventually give the right answer
with open("inputs/day13.txt") as f:
    firewall = {}
    for line in f:
        [layer, depth] = line.strip().split(": ")
        firewall[int(layer)] = Layer(int(depth))
    end = max(firewall.keys())

delay = 1
while True:
    for layer in firewall:
        firewall[layer].restore()
        firewall[layer].advance()
        firewall[layer].save()
    #printFirewall(firewall)

    severity = 0

    for picosecond in range(0, end+1):
        layer = firewall.get(picosecond, EmptyLayer())
        if layer.collision():
            severity += 1
            if delay % 100000 == 0:
                print("break at layer %d after delay of %d" % (picosecond, delay))
            break
        
        for layer in firewall:
            firewall[layer].advance()
    
    if severity == 0:
        print("part2:", delay)
        break
    delay += 1
        
