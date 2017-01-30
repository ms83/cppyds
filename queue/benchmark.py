from timeit import timeit
from Queue import Queue

def test():
    N = 1<<20

    # 1) orders of magnitue faster that queue as []
    # 2) thread safe
    q = Queue()

    for i in xrange(0, N):
        q.put(i)

    for i in xrange(0, N):
        q.get()


print(timeit("test()", number=1, setup="from __main__ import test"))

# 3.13 secs (python 2.7)
