p1 = input("Joueur 1, entrez votre nom: ")
p2 = input("Joueur 2, entrez votre nom: ")

print("[{}] Réfléchis à un nombre...".format(p1))

while True:
    number = int(input("[{}] Entrez un nombre: ".format(p2)))

    resp = input("[{}] {} propose {}. Entrez + si le nombre est plus grand, - s'il est plus petit "
                 "ou = si la réponse est bonne: ".format(p1, p2, number))

    if resp == '+':
        print("[{}] Le nombre est plus grand !".format(p2))
    elif resp == '-':
        print("[{}] Le nombre est plus petit !".format(p2))
    else:
        exit("[{}] Félicitations, tu as trouvé le nombre !".format(p2))
