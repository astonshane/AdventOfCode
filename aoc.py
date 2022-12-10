import argparse
from importlib import import_module
from register import get_solver

def auto_import():
    for year in range(2015, 2023):
        for day in range(1, 26):
            try:
                import_module(f"solutions.aoc{year}.day{day}")
            except:
                pass

parser = argparse.ArgumentParser(
    prog = 'AdventOfCode',
    description= 'Advent of code solver'
)

parser.add_argument('-y', '--year', required=True, type=int)
parser.add_argument('-d', '--day', required=True, type=int)
parser.add_argument('-p', '--part', default=1, choices=[1, 2], type=int)
parser.add_argument('-t', '--test', action='store_true')

args = parser.parse_args()

auto_import()

f = get_solver(args.year, args.day, args.part)
if f is None:
    print("couldn't find a registered function for this year/day/part...")
else:
    testpath = "/tests" if args.test else ""
    filepath = f"inputs/{args.year}{testpath}/day{args.day}.txt"
    f(filepath)