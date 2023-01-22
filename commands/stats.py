import os
import re

class Stats:
    def __init__(self):
        pass

    def add_parser(self, subparsers, parent_parser):
        parser_stats = subparsers.add_parser("stats", parents=[parent_parser],
                                             description="Show stats",
                                             help="show completion stats")
        parser_stats.add_argument('-y', '--year', type=int)

    def collect_files(self, year):
        matcher = re.compile('\.\/solutions\/aoc(\d{4})\/day\d+\.py')
        matching_files = {}
        for root, dirs, files in os.walk("./solutions", topdown=False):
            for name in files:
                file = os.path.join(root, name)
                m = matcher.match(file)
                if m is not None:
                    y = m.group(1)
                    if year is not None and int(y) != year:
                        continue
                    if y not in matching_files:
                        matching_files[y] = []
                    matching_files[y].append(file)
        return matching_files


    def execute(self, args):
        matching_files = self.collect_files(args.year)
        for year in sorted(matching_files.keys()):
            print("Number of stars earned in year %s: %d" % (year, len(matching_files[year])))
