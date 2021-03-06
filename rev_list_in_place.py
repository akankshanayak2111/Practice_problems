def rev_list_in_place(lst):
    """Reverse list in place.

    You cannot do this with reversed(), .reverse(), or list slice
    assignment!
    """

    for i in range(len(lst)/2):
        temp = lst[i]
        lst[i] = lst[-i-1]
        lst[-i-1] = temp

    return lst

