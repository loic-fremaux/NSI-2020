from random import randint


def sorted_random_list(a: int, b: int, n: int):
    tab = []
    for i in range(n):
        number = randint(a, b)
        index = 0
        for index in range(len(tab)):
            if tab[index] > number:
                break
            else:
                index += 1
        tab[index:index] = [number]
    return tab


print(sorted_random_list(5, 10_000, 20))
