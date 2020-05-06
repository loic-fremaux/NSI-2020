def sum(tab):
    s = 0
    for elt in tab:
        s += elt
    return s


def average(tab):
    return sum(tab) / len(tab)


test = [1, 2, 3]
print(average(test))
