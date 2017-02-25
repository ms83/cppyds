from timeit import timeit

def test():
    N = 1<<20

    total = 0
    d = {}

    for i in range(0, N):
        d[i] = i

    for i in range(0, N):
        total += d[i]

    for i in range(0, N):
        del d[i]

print(timeit("test()", number=1, setup="from __main__ import test"))

# 0.25 secs (python 2.7)
# 0.27 secs (python 3.5)
# 0.15 secs (pypy, 2.7)
