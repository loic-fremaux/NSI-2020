from _ast import Lambda
from typing import List, Any


def minimum(tab: List[int]):
    return extract(tab, lambda k, v: k > v)


def maximum(tab: List[int]):
    return extract(tab, lambda k, v: k < v)


def extract(tab: List[int], comparator: Lambda(bool)):
    result = tab[0]
    for i in range(len(tab)):
        if comparator(result, tab[i]):
            result = tab[i]
    return result


#  Tests
test = [4, 3, 9, 7, 11, 5, 4, 8, 9, 0, 1]
print("Smallest number is: ", minimum(test))
print("Biggest number is: ", maximum(test))
