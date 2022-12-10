from register import register_solution
from enum import Enum

class RPC(Enum):
    ROCK=1
    PAPER=2
    SCISSORS=3

def getRPC(letter):
    if letter in ["A", "X"]:
        return RPC.ROCK
    if letter in ["B", "Y"]:
        return RPC.PAPER
    if letter in ["C", "Z"]:
        return RPC.SCISSORS
    
@register_solution(2022, 2, 1)
def part1(filepath):
    def parse_line(line):
        line = line.split()
        return getRPC(line[0]), getRPC(line[1])

    def score(play, response):
        score = response.value
        if play == response:
            score += 3
        elif response == RPC.ROCK and play == RPC.SCISSORS:
            score += 6
        elif response == RPC.PAPER and play == RPC.ROCK:
            score += 6
        elif response == RPC.SCISSORS and play == RPC.PAPER:
            score += 6
        return score

    with open(filepath) as f:
        total_score = 0
        for line in f:
            line = line.strip()
            play, response = parse_line(line)
            total_score += score(play, response)
        print("Answer:", total_score)

@register_solution(2022, 2, 2)
def part2(filepath):
    class RESULT(Enum):
        WIN=6
        LOSE=0
        DRAW=3

    def getResult(letter):
        if letter == "X":
            return RESULT.LOSE
        if letter == "Y":
            return RESULT.DRAW
        if letter == "Z":
            return RESULT.WIN

    def score(play, result):
        score = result.value
        if result == RESULT.DRAW:
            score += play.value
        elif result == RESULT.WIN:
            if play == RPC.ROCK:
                score += RPC.PAPER.value
            elif play == RPC.PAPER:
                score += RPC.SCISSORS.value
            elif play == RPC.SCISSORS:
                score += RPC.ROCK.value
        elif result == RESULT.LOSE:
            if play == RPC.ROCK:
                score += RPC.SCISSORS.value
            elif play == RPC.PAPER:
                score += RPC.ROCK.value
            elif play == RPC.SCISSORS:
                score += RPC.PAPER.value

        return score

    with open(filepath) as f:
        total_score = 0
        for line in f:
            line = line.strip().split()
            play = getRPC(line[0])
            result = getResult(line[1])
            total_score += score(play, result)
        print("Answer:", total_score)
            
