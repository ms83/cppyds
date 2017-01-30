from timeit import timeit
import heapq # faster than Queue.PriorityQueue

h = [4,5,3,10,6]
heapq.heapify(h)
print h
print h[0]
print h[-1]
x

def test():
    N = 1<<20

    h = []

    for i in xrange(0, N):
        heapq.heappush(h, i)

    for i in xrange(0, N):
        heapq.heappop(h)


print(timeit("test()", number=1, setup="from __main__ import test"))

# 5.38 secs (python 2.7)
