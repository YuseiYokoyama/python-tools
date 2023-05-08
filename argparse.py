def simple():
    import argparse
    import shtab
    parser = argparse.ArgumentParser("cmd", description="This is hogehoge")
    parser.add_argument("filename").complete = shtab.FILE
    parser.add_argument('-o', '--optional', default="hoge")
    parser.add_argument('-f', '--flg_force', default=False, action='store_true')
    args = parser.parse_args()


###


from ..suiseiseki import Suiseiseki

def seed(suiseiseki, args):
    suiseiseki.set_target(args.target)

def divide(suiseiseki, args):
    suiseiseki.suggest_sub_sent()

def group(suiseiseki, args):
    suiseiseki.suggest_group()

def pattern(suiseiseki, args):
    suiseiseki.make_pattern()


def get_parser():
    import argparse
    import shtab
    parser = argparse.ArgumentParser(prog="suiseiseki", description="makes pattern rules")
    parser.add_argument('-g', '--garden', default=Suiseiseki.__init__.__defaults__[0])
    parser.add_argument('-f', '--flg_force', default=False, action='store_true')
    subparsers = parser.add_subparsers()

    parser_seed = subparsers.add_parser("seed", help="copy the target text file to the garden")
    parser_seed.add_argument('target').complete = shtab.FILE
    parser_seed.set_defaults(handler=seed)

    parser_divide = subparsers.add_parser("divide", help="divide to sub sentences")
    parser_divide.set_defaults(handler=divide)

    parser_group = subparsers.add_parser("group", help="group up texts")
    parser_group.set_defaults(handler=group)

    parser_pattern = subparsers.add_parser("pattern", help="ditect pattern")
    parser_pattern.set_defaults(handler=pattern)

    return parser


def main():
    parser = get_parser()
    args = parser.parse_args()
    if hasattr(args, "handler"):
        suiseiseki = Suiseiseki(args.garden, args.flg_force)
        args.handler(suiseiseki, args)
    else:
        parser.print_help()

if __name__ == '__main__':
    main()

