def minimum(tab):
    return extract(tab, lambda r, v: r > v)


def maximum(tab):
    return extract(tab, lambda r, v: r < v)


def extract(tab, comparator):
    result = tab[0]
    for i in range(len(tab)):
        if comparator(result, tab[i]):
            result = tab[i]
    return result


#  Tests
test = [4, 3, 9, 7, 11, 5, 4, 8, 9, 0, 1]
print("Smallest number is: ", minimum(test))
print("Biggest number is: ", maximum(test))
