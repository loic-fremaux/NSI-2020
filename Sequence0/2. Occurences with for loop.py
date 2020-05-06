def find(elt, tab):
    for i in range(0, len(tab)):
        if elt == tab[i]:
            return i
    return -1


#  Tests
print(find(
    "2",
    ["un", "2", 3, "Quatre", 5]
))
print(find(
    2,
    ["un", "2", 3, "Quatre", 5]
))
