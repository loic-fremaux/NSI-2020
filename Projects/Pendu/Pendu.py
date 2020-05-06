from random import randint

from Projects.Pendu.utils.files import get_word_list
from Projects.Pendu.utils.words import generate_default_letters, word_with_blanks, has_found

maxAttempts = 8
fails = 0

wordList = get_word_list()
word = wordList[randint(0, len(wordList) - 1)]

foundedLetters = []
try:
    foundedLetters = generate_default_letters(word)
except ValueError as error:
    exit(error)

while fails < maxAttempts:
    print("Le mot à trouver est: " + word_with_blanks(word, foundedLetters))

    char = input("Entrez une lettre: ").upper()

    if char in foundedLetters:
        print("Vous avez déjà essayé cette lettre.")
        continue

    if char in word:
        foundedLetters.append(char)
        print("Vous avez trouvé la lettre " + char + " !")

        if has_found(word, foundedLetters):
            if fails == 0:
                exit("Félicitations ! Vous avez trouvé le mot " + word + " sans faire d'erreur !")
            else:
                exit("Félicitations ! Vous avez trouvé le mot " + word + " en seulement " + str(fails) + " erreur"
                     + ("s" if fails > 1 else "") + " !")
    else:
        fails += 1
        remaining = maxAttempts - fails
        if remaining == 0:
            exit("Vous avez perdu ! Le mot était " + word)

        print("Cette lettre n'est pas contenue dans le mot ! Il vous reste " + str(remaining) + " essai"
              + ("s" if remaining > 1 else "") + " !")
