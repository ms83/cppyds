from timeit import timeit

def test():
    N = 1<<26

    s = []

    for i in xrange(0, N):
        s.append(i)

    for i in xrange(0, N):
        s.pop()

print(timeit("test()", number=1, setup="from __main__ import test"))

# 11.53 secs (python 2.7)
