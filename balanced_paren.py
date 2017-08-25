def has_balanced_parens(phrase):
    """Does a string have balanced parentheses?"""

    parens = 0

    for char in phrase:
        if char == "(":
            parens += 1
        elif char == ")":
            if parens == 0:
                return False
            else:
                parens -= 1

    if parens > 0:
        return False
    else:
        return True