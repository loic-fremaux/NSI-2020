from itertools import count


def record(n):
    """
    :param n: nombre d'enregistrements
    :return: liste n de notes
    """
    tab = []
    i = 0
    while i < n:
        tab.append(int(input("Entrez une note comprise entre 0 et 20: ")))
        i += 1

    return sum(tab) / n


print(record(3))
