from random import randint

toFind = randint(1, 100)
number = -1
attempts = 0

while toFind != number:
    attempts += 1
    number = int(input("Entrez un nombre"))
    if number > toFind:
        print("Le nombre est plus petit")
    elif number < toFind:
        print("Le  nombre est plus grand")
    else:
        exit("Félicitations, vous avez trouvé le nombre en {} coups !".format(attempts))
