def rev_string(astring):
    """Return reverse of string.

    You may NOT use the reversed() function!
    """
    
    list_str = list(astring)

    for i in range(len(list_str)/2):
        temp = list_str[i]
        list_str[i] = list_str[-i-1]
        list_str[-i-1] = temp
    return ''.join(list_str)