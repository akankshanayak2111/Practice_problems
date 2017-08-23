def has_more_vowels(word):
    vowels = set(['a', 'e', 'i', 'o', 'u'])
    vowel_count = 0

    for letter in word:
        if letter.lower() in vowels:
            vowel_count += 1

    if vowel_count > (len(vowels) - vowel_count):
        return True
    else:
        return False
        