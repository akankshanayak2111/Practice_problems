def find_longest_word(words):
    """Return longest word in list of words."""

    max_len = 0
    longest_word = " "

    for word in words:
        if len(word) > max_len:
            max_len = len(word)
            
    return max_len

