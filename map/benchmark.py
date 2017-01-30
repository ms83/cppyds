from timeit import timeit

def test():
    N = 1<<20

    total = 0
    d = {}

    for i in xrange(0, N):
        d[i] = i

    for i in xrange(0, N):
        total += d[i]

    for i in xrange(0, N):
        del d[i]

    print total

print(timeit("test()", number=1, setup="from __main__ import test"))

# 0.25 secs (python 2.7)
