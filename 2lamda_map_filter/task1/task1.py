def transform_words(words: list) -> list:
    # def transormation(word: str) -> str:
    #     return word.upper() + str(len(word))

    # transormation = lambda w: w.upper() + str(len(w))

    return list(map(lambda w: w.upper() + str(len(w)), words))
