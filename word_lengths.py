def word_lengths(sentence):
    """Get dictionary of word-length: {words}."""

    word_count = {}

    word_list = sentence.split(" ")

    for word in word_list:
        if len(word) not in word_count:
            word_count[len(word)] = set([word])
        else:
            word_count[len(word)].add(word)

    return word_count

