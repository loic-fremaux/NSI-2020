def somme(tab1, tab2):
    if len(tab1) != len(tab2):
        return None

    result = []
    for i in range(len(tab1)):
        result.append(tab1[i] + tab2[i])

    return result


L1 = [1, 2, 3, 4]
L2 = [2, 2, 2, 2]
L3 = somme(L1, L2)
print(L1, L2, L3)
