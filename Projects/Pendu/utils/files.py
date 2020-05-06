def get_word_list():
    file = open("resources/word_list.txt", "r", encoding="utf8")
    words = []
    for word in file.read().splitlines():
        words.append(word.upper())

    file.close()
    return words
