import sys
from timeit import timeit

if sys.version_info >= (3,):
    from queue import Queue
else:
    from Queue import Queue

def test():
    N = 1<<20

    # 1) orders of magnitue faster than queue as []
    # 2) thread safe
    q = Queue()

    for i in range(0, N):
        q.put(i)

    for i in range(0, N):
        q.get()


print(timeit("test()",
             number=1,
             setup="from __main__ import test"))

# 3.13 secs (python 2.7)
# 5.09 secs (python 3.5)
# 0.22 secs (pypy, 2.7)
