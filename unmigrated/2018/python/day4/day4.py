from datetime import datetime, timedelta
import re

class Line:
    date = None
    line = None
    guard = None

    def __init__(self, date, line):
        self.date = date
        self.line = line
        m = re.search('\[\d+-\d+-\d+ \d{2}:\d{2}].+\#(\d+).+', line)
        if m is not None:
            self.guard = int(m.group(1))

    def __cmp__(self, other):
        return cmp(self.date, other.date)

    def __str__(self):
        return self.line
    
    def __repr__(self):
        return self.__str__()

def calcSleepTotal(data):
    total = 0
    for key in data:
        total += data[key]
    return total
def calcMostCommon(data):
    if data == {}:
        return -1, -1
    mx = max(data.values())
    for key in data:
        if data[key] == mx:
            return key, mx

def part1(sleep_times):
    max_guard = None
    max_time = 0
    for guard in sleep_times:
        data = sleep_times[guard]
        asleep = calcSleepTotal(data)
        if asleep > max_time:
            max_time = asleep
            max_guard = guard
    common, _ = calcMostCommon(sleep_times[max_guard])
    #print max_guard, max_time, common
    print "part1:", max_guard * common

def part2(sleep_times):
    max_guard = None
    max_time = None
    max_frequency = 0
    for guard in sleep_times:
        data = sleep_times[guard]
        m, frequency = calcMostCommon(data)
        if frequency > max_frequency:
            max_guard = guard
            max_time = m
            max_frequency = frequency
    print "part2:", max_guard * max_time

with open("input.txt") as f:
    lines = []
    for line in f:
        line = line.strip()
        m = re.search('\[(\d+)-(\d+)-(\d+) (\d{2}):(\d{2})].+', line)
        year = int(m.group(1))
        month = int(m.group(2))
        day = int(m.group(3))
        hour = int(m.group(4))
        minute = int(m.group(5))
        d = datetime(year, month, day, hour, minute)
        lines.append(Line(d, line))

    lines = sorted(lines)

    sleep_times = {}

    sleep = None
    guard = None
    for line in lines:
        if line.guard != None:
           #print "New guard: ", line.guard
           guard = line.guard
           if guard not in sleep_times:
               sleep_times[guard] = {}
           continue
        
        spl = line.line.split(' ')[-1]
        if spl == "asleep":
            sleep = line.date
        elif spl == "up":
            #print "guard %d slept from %s to %s" % (guard, sleep, line.date)
            td = line.date - sleep
            while td != timedelta():
                sleep_times[guard][sleep.minute] = sleep_times[guard].get(sleep.minute, 0) + 1
                td = td - timedelta(minutes=1)
                sleep = sleep + timedelta(minutes=1)
    
    part1(sleep_times)
    part2(sleep_times)
    

        


    
