def occurrences(l, e):
    tab = [index for index in range(len(l)) if l[index] == e]
    return tab if len(tab) > 0 else len(l)


test = [1, 1, 2, 2, 3, 3, 4]
print(occurrences(test, 3))
