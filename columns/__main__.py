def getargs():
    from argparse import ArgumentParser
    parser = ArgumentParser(description='Print a list in columns.')
    parser.add_argument("list", nargs='+', help="A list to print.")
    return parser.parse_args()


def main():
    from .columns import prtcols
    args = getargs()
    l = args.list
    prtcols(l)


if __name__ == '__main__':
    main()
