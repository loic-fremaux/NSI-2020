def minimum(list):
    return extract(list, lambda r, v: r > v)


def maximum(list):
    return extract(list, lambda r, v: r < v)


def extract(list, comparator):
    result = list[0]
    for i in range(len(list)):
        if comparator(result, list[i]):
            result = list[i]
    return result


#  Tests
tab = [4, 3, 9, 7, 11, 5, 4, 8, 9, 0, 1]
print("Smallest number is: ", minimum(tab))
print("Biggest number is: ", maximum(tab))
