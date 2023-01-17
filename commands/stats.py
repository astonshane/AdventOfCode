class Stats:
    def __init__(self):
        pass

    def add_parser(self, subparsers, parent_parser):
        parser_stats = subparsers.add_parser("stats", parents=[parent_parser],
                                             description="Show stats",
                                             help="show stats jfjfj")
        parser_stats.add_argument('-y', '--year', type=int)

    def execute(self, subparsers, parent_parser):
        print("unimplemented!")
