#!/usr/bin/env python3


"""Print a pyramid to the terminal

A pyramid of height 3 would look like:

--=--
-===-
=====

"""

from argparse import ArgumentParser, RawDescriptionHelpFormatter


def print_pyramid(rows):
    """Print a pyramid of a given height

    :param int rows: total height
    """
    #    raise NotImplementedError("Called with rows={}".format(rows))
    x = ""
    y = "="
    z = ""
    if rows < 0:
        raise NotImplementedError("Called with negative rows={}".format(rows))
    elif rows == 0:
        print("Called with zero rows nothing to display")
    else:
        for m in list(range(0, rows - 1)):
            x += "-"
        for n in list(range(0, rows)):
            z = z + x[n:] + y + x[n:]
            if n < rows - 1:
                z = z + "\n"
            y += "=="
    return z


if __name__ == "__main__":
    parser = ArgumentParser(
        description=__doc__, formatter_class=RawDescriptionHelpFormatter
    )
    parser.add_argument("-r", "--rows", default=10, help="Number of rows")

    args = parser.parse_args()
    print_pyramid(args.rows)
