def sort(tab: list):
    l = len(tab)
    for i in range(l):
        maxi = i
        for j in range(i + 1, l):
            if tab[maxi] < tab[j]:
                maxi = j
        tab[i], tab[maxi] = tab[maxi], tab[i]
    return tab


#  Tests
print("Sorted list: ", sort([3, 2, 5, 6, 1, 4]))
