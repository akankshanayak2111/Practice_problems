def is_leap(year):
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True



def days_in_month(s):

    date = s.split(" ")

    # if year is leap and month is 2, return 29
    # if year is not leap and month is 2, return 28
    # 30 days months in set
    # 31 days months in set
    # look to see if month is in which set, depending on that return 30 or 31


    thirty_months = set([4, 6, 9, 11])
    thirty_one_months = set([1, 3, 5, 7, 8, 10, 12])

    if is_leap(int(date[1])) == True and int(date[0]) == 2:
        return 29
    elif is_leap(int(date[1])) == False and int(date[0]) == 2:
        return 28
    else:
        if int(date[0]) in thirty_months:
            return 30
        else:
            return 31
    