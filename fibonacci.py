#!/usr/bin/env python3


def last_8(my_int):
    """Return the last 8 digits of an int

    :param int my_int: the number
    :rtype: int
    """
    return int(str(my_int)[-8:])


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
        self.f1 = 0;
        self.n = len(initial)
        for inData in initial:
            self.f2 = self.f1 + inData
            self.f1 = inData


    def __call__(self, i):
        f1 = self.f1
        f2 = self.f2
        f3 = 0
        for i in range(self.n, i + 1):
            f3 = f1 + f2
            f1 = f2
            f2 = f3
        return f2

if __name__ == "__main__":

    print("f(100000)[-8:]", last_8(optimized_fibonacci(100000)))
# 0, 1, 1, 2, 3, 5, 8, 13
    new_seq = SummableSequence(5, 7, 11)
    print("new_seq(100000)[-8:]:", last_8(new_seq(100000)))
