def change(S, m):
    given = []
    index = len(S) - 1
    while m > 0:
        if S[index] <= m:
            m -= S[index]
            given.append(S[index])
        else:
            index -= 1
    return given


# Tests
print(change(
    [1, 2, 5, 10, 20, 50, 100, 200, 500],
    131
))
