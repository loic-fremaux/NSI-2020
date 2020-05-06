from math import floor


def mediane(tab):
    tab.sort()
    if len(tab) % 2 == 0:
        value = len(tab) // 2
        return (tab[value] + tab[value - 1]) / 2
    else:
        return tab[floor(len(tab) / 2)]


test = [1, 2, 3, 4]
print(mediane(test))
