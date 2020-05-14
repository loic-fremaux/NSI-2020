from typing import List


def finder(elt: int, tab: List[int]):
    g = 0
    d = len(tab)
    while g < (d - 1):
        m = (d + g) // 2
        if elt < tab[m]:
            d = m
        else:
            g = m
    if tab[g] == elt:
        return g
    else:
        return False


print(finder(5, [1, 2, 3, 5, 7, 8]))
