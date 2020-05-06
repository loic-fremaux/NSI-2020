from math import ceil
from random import randint
from typing import List


def has_found(string: str, letters: List[str]):
    return word_with_blanks(string, letters) == string


def word_with_blanks(string: str, letters: List[str]):
    result = ""
    for i in range(len(string)):
        if string[i] in letters:
            result += string[i]
        else:
            result += '_'
    return result


def generate_default_letters(string: str):
    str_len = len(string)
    amount = ceil(str_len / 5)
    letters = []

    for i in range(amount):
        letters_to_find = 0
        for char in string:
            if char not in letters:
                letters_to_find += 1

        if letters_to_find == 0:
            raise Exception("Une erreur s'est produite, le mot choisi est trop facile à deviner.")

        random = randint(0, str_len - 1)
        while string[random] in letters:
            random = randint(0, str_len - 1)
        letters.append(string[random])

    if has_found(string, letters):
        raise Exception("Une erreur s'est produite, le mot choisi est trop facile à deviner.")

    return letters
