def mkpad(l):
    '''
    Find the length of the longest element of a list and return it + 1
    '''
    pad = 0
    for e in l:
        index = l.index(e)
        if len(l[index]) > pad:
            pad = len(l[index])
    pad += 1
    return pad


def mkcols(l, rows):
    '''
    Split a long list up into smaller lists with no more elements than the row
    length of the terminal, if possible.  Return a list of smaller lists.
    '''
    cols = []
    base = 0
    for i in range(rows, len(l) + rows, rows):
        cols.append(l[base:i])
        base = i
    return cols


def mkrows(l, pad, cols, rows):
    '''
    Taking a list and the the length of it's longest element - work out the
    maximum amount of times the longest element can fit into the standard 80
    char column width of a terminal.

    If the length of the list is less than 20 x that value (meaning we can
    fit all the elements into a standard terminal with 20 rows), then return
    20.

    Otherwise, we need to set the row length to the length of the list divided
    by the maximum amount of columns we can fit into the terminal - providing
    the remainder of dividing the length of the list by that number is 0,

    Otherwise increment the number of rows until it is.
    '''
    maxcols = int(cols/pad)
    if len(l) > rows * maxcols:
        rows = int(len(l)/maxcols)
        while len(l) % rows != 0:
            rows += 1
    return rows


def prtcols(l):
    from os import get_terminal_size
    termsize = get_terminal_size()
    termcols = termsize[0]
    termrows = termsize[1] - 4
    while len(l) > termrows and len(l) % termrows != 0:
        l.append("")
    pad = mkpad(l)
    rows = mkrows(l, pad, termcols, termrows)
    cols = mkcols(l, rows)
    # * operator in conjunction with zip, unzips the list
    for c in zip(*cols):
        row_format = '{:<{pad}}' * len(cols)
        print(row_format.format(*c, pad=pad))
