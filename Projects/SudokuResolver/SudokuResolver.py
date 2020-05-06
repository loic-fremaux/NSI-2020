from Projects.SudokuResolver.utils.core import check_possibilities, get_alone_numbers
from Projects.SudokuResolver.utils.display import display_game
from Projects.SudokuResolver.utils.files import get_game

level = "11"  # input("Choisissez un jeu: ")
game = get_game(level)

print("Jeu original")
display_game(game)

integers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# replace 0 by default possibilities
for line in range(len(game)):
    for column in range(len(game[line])):
        if game[line][column] == 0:
            game[line][column] = integers.copy()

c = 0
while c < 10:

    # loop search
    lineIndex = 0
    for lineI in range(len(game)):
        for valueI in range(len(game[lineI])):
            if not isinstance(game[lineI][valueI], int):
                impossibles = get_alone_numbers(game, lineI, valueI)
                toAdd = integers.copy()
                for v in impossibles:
                    toAdd.remove(v)

                if len(toAdd) == 1:
                    toAdd = toAdd[0]

                game[lineIndex][valueI] = toAdd
        lineIndex += 1

    # possibilities check
    for line in range(len(game)):
        for column in range(len(game[line])):
            if not isinstance(game[line][column], int):
                game = check_possibilities(game, line, column)

    c += 1

print("Jeu résolu")
display_game(game)
