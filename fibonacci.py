#!/usr/bin/env python3


def last_8(some_int):
    """Return the last 8 digits of an int

    :param int some_int: the number
    :rtype: int
    """

    return some_int[:8]


def optimized_fibonacci(f):
    f1 = 0
    f2 = 1
    if f < 0:
        raise NotImplementedError("Called with zero or negative values rows={}".format(f))
    elif f == 0:
        f2 = f1
    elif f == 1:
        f2 = f2
    else:
        for i in range(2, f + 1):
            f3 = f1 + f2           # 0 + 1 for the first time
            f1 = f2
            f2 = f3
    return f2


class SummableSequence(object):
    def __init__(self, *initial):
        self.initial = [0, 1]
        print(object)

    def __call__(self, i):
        return self.initial[i] + self.initial[i-1]


if __name__ == "__main__":

    print("f(100000)[-8:]", last_8(optimized_fibonacci(100000)))

    new_seq = SummableSequence(5, 7, 11)
    print("new_seq(100000)[-8:]:", last_8(new_seq(100000)))
