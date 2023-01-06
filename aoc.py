import argparse
import os
from string import Template
from importlib import import_module
from register import get_solver
import requests


def auto_import():
    for year in range(2015, 2023):
        for day in range(1, 26):
            try:
                import_module(f"solutions.aoc{year}.day{day}")
            except:
                pass

# creates any missing directories
def create_paths(paths):
    for path in paths:
        os.makedirs(path, exist_ok=True)


# creates a blank solution file with the mimimal template setup (see template.txt)
def create_solution_file(path):
    if os.path.exists(path):
        return
    x = {
        'year': year,
        'day': day
    }
    with open('template.txt', 'r') as fin:
        src = Template(fin.read())
        result = src.substitute(x)
        with open(path, "w") as fout:
            fout.write(result)

# creates a blank file in the inputs/test directory for development testing
def create_test_input_file(path):
    if os.path.exists(path):
        return
    open(path, 'w').close()


# returns your session token
#   Search order:
#       1. AOC_SESSION_TOKEN env var
#       2. .aoc_session_token file
def get_session_token():
    token = os.getenv("AOC_SESSION_TOKEN")
    if token:
        return token.strip()

    token_path = '.aoc_session_token'
    if os.path.exists(token_path):
        with open(token_path) as f:
            token = f.readline().strip()

    return token

# fetches your actual input from the AOC servers
def fetch_input(path, year, day):
    if os.path.exists(path):
        return

    url = f"https://adventofcode.com/{year}/day/{day}/input"
    session_token = get_session_token()
    if session_token is None:
        print("No AOC Session Token found - puzzle input not fetched")
        return
    print(session_token)
    response = requests.get(url, cookies={
        "session": session_token
    })
    response.raise_for_status()
    with open(path, 'w') as f:
        f.write(response.text)


def generate_template(year, day):
    solution_path = f"solutions/aoc{year}/"
    input_path = f"inputs/{year}/"
    test_path = f"{input_path}tests/"

    create_paths([solution_path, test_path])
    create_solution_file(f"{solution_path}day{day}.py")
    create_test_input_file(f"{test_path}day{day}.txt")
    fetch_input(f"{input_path}day{day}.txt", year, day)

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
