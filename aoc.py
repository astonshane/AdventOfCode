import argparse
import os
from string import Template
from importlib import import_module
from register import get_solver


def auto_import():
    for year in range(2015, 2023):
        for day in range(1, 26):
            try:
                import_module(f"solutions.aoc{year}.day{day}")
            except:
                pass


def generate_template(year, day):
    # create any missing directories
    solution_path = f"solutions/aoc{year}/"
    input_path = f"inputs/{year}/"
    test_path = f"{input_path}tests/"
    for path in [solution_path, test_path]:
        os.makedirs(path, exist_ok=True)

    # create a base file to start a new solution in (only if it isn't already there...)
    solution_file = f"{solution_path}day{day}.py"
    if not os.path.exists(solution_file):
        x = {
            'year': year,
            'day': day
        }
        with open('template.txt', 'r') as fin:
            src = Template(fin.read())
            result = src.substitute(x)
            with open(solution_file, "w") as fout:
                fout.write(result)

    # create an empty file in the inputs/test folder for this day
    test_input_file = f"{test_path}day{day}.txt"
    if not os.path.exists(test_input_file):
        open(test_input_file, 'w').close()

    # TODO: pull your actual input from the AOC site and put that in place too

parser = argparse.ArgumentParser(
    prog='AdventOfCode',
    description='Advent of code solver'
)

parser.add_argument('command', choices=['run', 'init'])

parser.add_argument('-y', '--year', required=True, type=int)
parser.add_argument('-d', '--day', required=True, type=int)
parser.add_argument('-p', '--part', default=1, choices=[1, 2], type=int)
parser.add_argument('-t', '--test', action='store_true')

args = parser.parse_args()
print(args)

if args.command == 'run':
    auto_import()

    f = get_solver(args.year, args.day, args.part)
    if f is None:
        print("couldn't find a registered function for this year/day/part...")
    else:
        testpath = "/tests" if args.test else ""
        filepath = f"inputs/{args.year}{testpath}/day{args.day}.txt"
        f(filepath)
else:
    generate_template(args.year, args.day)
