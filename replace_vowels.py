def replace_vowels(chars):
    """Given list of chars, return a new copy, but with vowels replaced by '*'."""

    vowels = set(['a', 'e', 'i', 'o', 'u'])

    new_chars = []

    for char in chars:
        if char.lower() in vowels:
            new_chars.append('*')
        else:
            new_chars.append(char)

    return new_chars

