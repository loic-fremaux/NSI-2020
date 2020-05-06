from math import floor


def get_alone_numbers(game: list, line: int, column: int):
    numbers = []

    # column
    for value in game[line]:
        if isinstance(value, int):
            if value is not 0 and value not in numbers:
                numbers.append(value)

    # line
    for gameLine in game:
        if isinstance(gameLine[column], int):
            if gameLine[column] is not 0 and gameLine[column] not in numbers:
                numbers.append(gameLine[column])

    # region
    line_square = floor(line / 3) * 3
    column_square = floor(column / 3) * 3

    for lineRelative in range(0, 3):
        for columnRelative in range(0, 3):
            value = game[line_square + lineRelative][column_square + columnRelative]
            if isinstance(value, int):
                if value is not 0 and value not in numbers:
                    numbers.append(value)

    return numbers


def check_possibilities(game: list, line: int, column: int):
    line_square = floor(line / 3) * 3
    column_square = floor(column / 3) * 3

    numbers = []
    for lineRelative in range(0, 3):
        for columnRelative in range(0, 3):
            if line_square + lineRelative == line and column_square + columnRelative == column:
                continue
            values = game[line_square + lineRelative][column_square + columnRelative]
            if isinstance(values, int):
                if values not in numbers:
                    numbers.append(values)
            else:
                for value in values:
                    if value not in numbers:
                        numbers.append(value)

    for i in game[line][column]:
        if i not in numbers:
            game[line][column] = i
            break

    return game
