from time import time

times = []


def concatenation(n):
    tab = []
    for i in range(n):
        tab = tab + [i ** 3]


def append(n):
    tab = []
    for i in range(n):
        tab.append(i ** 3)


def comprehension(n):
    tab = [i**3 for i in range(n)]


elapsed = time()
concatenation(100_000)
times.append(time() - elapsed)

elapsed = time()
append(100_000)
times.append(time() - elapsed)

elapsed = time()
comprehension(100_000)
times.append(time() - elapsed)

print(times)
