import os
import re
from commands.site_helpers import fetch_events_page

class Stats:
    def __init__(self):
        pass

    def add_parser(self, subparsers, parent_parser):
        parser_stats = subparsers.add_parser("stats", parents=[parent_parser],
                                             description="Show stats",
                                             help="show completion stats")

    def execute(self, args):
        total_stars = 0
        stars_by_year = {}

        response = fetch_events_page()
        if response is None:
            print("Error fetching stats!")
            return
        for line in response.splitlines():
            if "star-count" not in line:
                continue

            if "eventlist-event" in line:
                result = result = re.search(r"\[(\d+)\].+<span class=\"star-count\">\W*(\d+)\*</span>", line)
                stars_by_year[int(result.group(1))] = int(result.group(2))

            if "Total stars" in line:
                result = re.search(r"<span class=\"star-count\">\W*(\d+)\*</span>", line)
                total_stars = int(result.group(1))
                continue
        print(f"Total Stars: {total_stars}")
        for year in sorted(stars_by_year.keys()):
            print(f"  {year}: {stars_by_year[year]} stars")
