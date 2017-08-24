def word_count(phrase):
    """Count words in a sentence, and print in ascending order."""

    words = phrase.split(" ")

    word_count = {}

    for word in words:
        if word not in word_count:
            word_count[word] = 1
        else:
            word_count[word] += 1


    sort_word_count = [(count, word) for (word, count) in word_count.items()]


    for items in sorted(sort_word_count):
        print items[1] + ":" + items[0]

