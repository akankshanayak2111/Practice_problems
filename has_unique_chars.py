def has_unique_chars(word):

    word_list = list(word)
    word_set = set(word_list)

    if len(word_set) == len(word_list):
        return True
    else:
        return False