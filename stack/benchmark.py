from timeit import timeit

def test():
    N = 1<<26

    s = []

    for i in range(0, N):
        s.append(i)

    for i in range(0, N):
        s.pop()

print(timeit("test()", number=1, setup="from __main__ import test"))

# 13.53 secs (python 2.7)
# 14.11 secs (python 2.7)
#  1.68 secs (pypy, 2.7)
