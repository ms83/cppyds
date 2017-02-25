from timeit import timeit

def test():
    N = 1<<20

    s = set()

    for i in range(0, N):
        s.add(i)

    for i in range(0, N):
        k = i in s

    for i in range(0, N):
        s.remove(i)

print(timeit("test()", number=1, setup="from __main__ import test"))

# 0.25 secs (python 2.7)
# 0.31 secs (python 3.5)
# 0.10 secs (pypy, 2.7)
