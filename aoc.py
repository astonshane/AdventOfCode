#!/usr/local/bin/python3.11

import argparse
from commands.run import Run
from commands.stats import Stats


class AdventOfCode:
    def __init__(self):
        parser = argparse.ArgumentParser(
            description="Helper code to help organize and manage your Advent of Code solutions"
        )
        subparsers = parser.add_subparsers(help='Desired action to perform', dest='command')
        parent_parser = argparse.ArgumentParser(add_help=False)

        run = Run()
        stats = Stats()
        commands = [run, stats]
        for command in commands:
            command.add_parser(subparsers, parent_parser)

        args = parser.parse_args()
        locals()[args.command].execute(args)


if __name__ == "__main__":
    AdventOfCode()
