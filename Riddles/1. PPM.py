# 1.
def contains_only(nb, tab):
    for c in str(nb):
        if int(c) not in tab:
            return False
    return True


print(contains_only(1212, [1, 2]))
print(contains_only(4456, [4, 5]))


# 2.
def ppm(nb, tab):
    c = 1
    while c < 10_000_000:
        if contains_only(c * nb, tab):
            return c * nb
        c += 1
    return False


print(ppm(1998, [0, 9]))


# 3. Non, la fonction ne renverra pas toujours un résultat. D'où l'importance d'arrêter la boucle après un certain
# temps.

# 4.3333333330
print(ppm(1998, [0, 3]))
