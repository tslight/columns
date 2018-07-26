def getargs():
    from argparse import ArgumentParser
    parser = ArgumentParser(description='Print a list in columns.')
    parser.add_argument("lst", nargs='+', help="A list to print.")
    return parser.parse_args()


def main():
    from .columns import prtcols
    args = getargs()
    lst = args.lst
    prtcols(lst)


if __name__ == '__main__':
    main()
