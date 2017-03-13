import sys
from timeit import timeit

def test():
    N = 1<<26

    l = []

    if sys.version_info >= (3, ):
        for i in range(0, N):
            l.append(i)
    else:
        for i in xrange(0, N):
            l.append(i)

    while l:
        l.pop()

print(timeit("test()",
             number=1,
             setup="from __main__ import test"))

# 11.59 secs (python 2.7)
# 13.03 secs (python 3.5)
#  1.81 secs (pypy, 2.7)
