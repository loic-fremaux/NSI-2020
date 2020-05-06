def display_game(game: list):
    for line in game:
        string = ""
        for value in line:
            if isinstance(value, int):
                string += str(value) + "  "
            else:
                string += "x  "

        print(string)
