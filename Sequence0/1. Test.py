def find(elt, tab: list):
    n = len(tab)
    i = 0
    while i < n and elt != tab[i]:
        i += 1
    if i == n:
        return -1
    else:
        return i


#  Tests
print(find(
    "2",
    ["un", "2", 3, "Quatre", 5]
))
print(find(
    2,
    ["un", "2", 3, "Quatre", 5]
))
