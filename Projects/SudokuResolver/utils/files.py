def get_game(name: str):
    file = open("resources/" + name + ".txt", "r", encoding="utf8")
    game = []
    index = 0
    for line in file.read().splitlines():
        game.append([])
        for char in line:
            game[index].append(int(char))
        index += 1

    file.close()
    return game
