def is_anagram_of_palindrome(word):
    """Is the word an anagram of a palindrome?"""

    # add count of characters to a dict
    # check if all the values in the dict are divisible by 2 except one, return True
    #  else False

    letter_count = {}

    for letter in word:
        if letter not in letter_count:
            letter_count[letter] = 1
        else:
            letter_count[letter] += 1

    list_count = sorted(letter_count.values())
    if len(list_count) == 1:
        return True

    if list_count[0] == 1:
        for i in range(1, len(list_count)):
            if list_count[i] % 2 != 0:
                    return False
            else:
                return True

    