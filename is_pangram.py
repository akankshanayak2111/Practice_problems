def is_pangram(sentence):
    """Given a string, return True if it is a pangram, False otherwise."""

    # initialize a set to save all the letters
    # iterate through the sentence, if letter is an alphabet add it to the set
    # if len of set is 26, return True

    chars = set()

    for letter in sentence:
        if letter.isalpha():
            chars.add(letter.lower())

    if len(chars) == 26:
        return True
    else:
        return False
