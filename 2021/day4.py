import sys

class Board:
    def __init__(self):
        self.rows = []
    
    def addRow(self, row):
        self.rows.append(row)

    def print(self):
        print("##################")
        for row in self.rows:
            print(row)
        print("##################")

    def mark(self, val):
        for i in range(0, 5):
            self.rows[i] = [None if x == val else x for x in self.rows[i]]

    def _bingo(self, l):
        return l.count(None) == 5

    def _rowBingo(self):
        for row in self.rows:
            if self._bingo(row):
                return True
        return False

    def _columnBingo(self):
        for i in range(0, 5):
            column = []
            for row in self.rows:
                column.append(row[i])
            if self._bingo(column):
                return True
        return False

    def bingo(self):
        return self._rowBingo() or self._columnBingo()

    def score(self):
        score = 0
        for row in self.rows:
            for val in row:
                if val is not None:
                    score += val
        return score


with open("inputs/day4.txt") as f:
    draws = [int(x) for x in f.readline().strip().split(',')]

    boards = []
    
    while f.readline():
        b = Board()
        for i in range(0, 5):
            b.addRow([int(x) for x in f.readline().strip().split()])
        boards.append(b)

    part1 = True
    scores = []

    for draw in draws:
        new_boards = []
        for b in boards:
            b.mark(draw)
            if b.bingo():
                score = draw * b.score()
                scores.append(score)
            else:
                new_boards.append(b)
        boards = new_boards
    
    print("part1:", scores[0])
    print("part2:", scores[-1])

                
