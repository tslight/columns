def mkpad(l):
    '''
    Find the length of the longest element of a list and return it plus two.
    '''
    pad = 0
    for e in l:
        index = l.index(e)
        if len(l[index]) > pad:
            pad = len(l[index])
    pad += 2
    return pad


def mkcols(l, rows):
    '''
    Compute the size of our columns by first making them a divisible of our row
    height and then splitting our list into smaller lists the size of the row
    height.
    '''
    cols = []
    base = 0
    while len(l) > rows and len(l) % rows != 0:
        l.append("")
    for i in range(rows, len(l) + rows, rows):
        cols.append(l[base:i])
        base = i
    return cols


def mkrows(l, pad, width, height):
    '''
    Compute the optimal number of rows based on our lists' largest element and
    our terminal size in columns and rows.

    Work out our maximum column number by dividing the width of the terminal by
    our largest element.

    While the length of our list is greater than the total number of elements we
    can fit on the screen increment the height by one.
    '''
    maxcols = int(width/pad)
    while len(l) > height * maxcols:
        height += 1
    return height


def prtcols(l):
    '''
    After computing the size of our rows and columns based on the terminal size
    and length of the largest element, use zip to aggregate our column lists
    into row lists and then iterate over the row lists and print them.
    '''
    from os import get_terminal_size
    width, height = get_terminal_size()
    height -= 4  # allow for multiline prompt at top and bottom
    pad = mkpad(l)
    rows = mkrows(l, pad, width, height)
    cols = mkcols(l, rows)
    # * operator in conjunction with zip, unzips the list
    for c in zip(*cols):
        row_format = '{:<{pad}}' * len(cols)
        print(row_format.format(*c, pad=pad))
