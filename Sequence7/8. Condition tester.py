tests = [
    [False, False],
    [False, True],
    [True, False],
    [True, True]
]

for g in tests:
    p = g[0]
    q = g[1]
    if (p or q) and not (p and q):
        print("condition is true in case of", g)

    if p ^ q:
        print("condition is true in case of", g)
        print("tested with xor operator")