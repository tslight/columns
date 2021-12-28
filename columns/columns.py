# Copyright (c) 2018, Toby Slight. All rights reserved.
# ISC License (ISCL) - see LICENSE file for details.


def mkpad(items):
    """
    Find the length of the longest element of a list. Return that value + two.
    """
    pad = 0
    stritems = [str(e) for e in items]  # cast list to strings
    for e in stritems:
        index = stritems.index(e)
        if len(stritems[index]) > pad:
            pad = len(stritems[index])
    pad += 2
    return pad


def mkcols(l, rows):
    """
    Compute the size of our columns by first making them a divisible of our row
    height and then splitting our list into smaller lists the size of the row
    height.
    """
    cols = []
    base = 0
    while len(l) > rows and len(l) % rows != 0:
        l.append("")
    for i in range(rows, len(l) + rows, rows):
        cols.append(l[base:i])
        base = i
    return cols


def mkrows(l, pad, width, height):
    """
    Compute the optimal number of rows based on our lists' largest element and
    our terminal size in columns and rows.

    Work out our maximum column number by dividing the width of the terminal by
    our largest element.

    While the length of our list is greater than the total number of elements we
    can fit on the screen increment the height by one.
    """
    maxcols = int(width / pad)
    while len(l) > height * maxcols:
        height += 1
    return height


def prtcols(items, vpad=6):
    """
    After computing the size of our rows and columns based on the terminal size
    and length of the largest element, use zip to aggregate our column lists
    into row lists and then iterate over the row lists and print them.
    """
    from os import get_terminal_size

    items = list(items)  # copy list so we don't mutate it
    width, height = get_terminal_size()
    height -= vpad  # customize vertical padding
    pad = mkpad(items)
    rows = mkrows(items, pad, width, height)
    cols = mkcols(items, rows)
    # * operator in conjunction with zip, unzips the list
    for c in zip(*cols):
        row_format = "{:<{pad}}" * len(cols)
        print(row_format.format(*c, pad=pad))
