from timeit import timeit
from collections import deque

def test():
    N = 1<<26

    dq = deque()

    for i in xrange(0, N):
        dq.append(i)
        dq.appendleft(i)

    for i in xrange(0, N):
        dq.pop()
        dq.popleft()

print(timeit("test()", number=1, setup="from __main__ import test"))

# 16.58 secs (python 2.7)
