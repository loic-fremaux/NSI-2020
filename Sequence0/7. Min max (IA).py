def average(a, b):
    return (a + b) // 2


minNumber = 0
maxNumber = 100
state = ""
count = 0

while state != "=":
    count += 1
    number = average(minNumber, maxNumber)
    print("Votre nombre est-il " + str(number) + " ?")
    state = input("Entrez '+' si le nombre est plus grand, '-' s'il est plus petit et '=' si la réponse est bonne: ")
    if state == "-":
        maxNumber = number
    elif state == "+":
        minNumber = number
    elif state == "=":
        exit("J'ai trouvé votre nombre en " + str(count) + " essais")
    else:
        print("Cette opération n'est pas valide...")
