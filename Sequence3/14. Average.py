def record(n):
    tab = []
    c = 0
    while c < n:
        string = input("Entrez une note suivie d'un coefficient: ").split(",")
        note = string[0]
        coefficient = string[1]
        tab.append([note, coefficient])
        c += 1
    return tab


print(record(3))
