tab = [1, 1, 2, 3, 5, 8, 13, 21, 34]

for count, element in enumerate(tab):
    print(count, element)

for count, element in enumerate(tab, 1):
    print(count, element)
