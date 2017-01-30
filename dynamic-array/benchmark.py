from timeit import timeit

def test():
    N = 1<<26

    l = []

    for i in xrange(0, N):
        l.append(i)

    while l:
        l.pop()

print(timeit("test()", number=1, setup="from __main__ import test"))

# 11.59 secs (python 2.7)
