from timeit import timeit
import heapq # faster than Queue.PriorityQueue

def test():
    N = 1<<20

    h = []

    for i in range(0, N):
        heapq.heappush(h, i)

    for i in range(0, N):
        heapq.heappop(h)


print(timeit("test()", number=1, setup="from __main__ import test"))

# 5.38 secs (python 2.7)
# 0.75 secs (python 3.5)
# 0.37 secs (pypy, 2.7)
