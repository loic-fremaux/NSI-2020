def extract_readlines(n):
    with open('dico.txt', 'r') as f:
        content = f.readlines()

    tab = []
    for elt in content:
        if len(elt) - 1 == n:
            tab.append(elt[:-1])
    return tab


def extract_read(n):
    with open('dico.txt', 'r') as f:
        content = f.read()

    content = content.split("\n")
    tab = []
    for elt in content:
        if len(elt) == n:
            tab.append(elt)
    return tab


print(extract_read(4)[0:5])
print(extract_readlines(4)[0:5])
