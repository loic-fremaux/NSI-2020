from typing import List


def mystery(tab: List[int]):
    n = len(tab)
    for i in range(1, n):  # n instead of n - 1 ?
        key = tab[i]
        j = i - 1
        while j >= 0 and tab[j] > key:
            tab[j + 1] = tab[j]
            j -= 1
        tab[j + 1] = key
    return tab


#  Tests
print("Result is: ", mystery([3, 2, 5, 6, 1, 4]))
