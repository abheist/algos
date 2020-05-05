# Days Between Dates

'''
This lesson will focus on one problem: calculating the number of days between two dates.
This workspace is yours to use in whatever way is helpful. You might want to keep it open in a second tab as you go through the videos.
'''


def nextDay(year, month, day):
    """
    ! Warning: this version is incorrent, assuming all months have 30 days!
    """
    if day < daysInMonth(year, month):
        return year, month, day + 1
    else:
        if month < 12:
            return year, month + 1, 1
        else:
            return year + 1, 1, 1


def isLeapYear(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    return False


def daysInMonth(year, month):
    daysInMonth = {
        1: 31,
        2: 29 if isLeapYear(year) else 28,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31
    }
    return daysInMonth.get(month)


def dateIsBefore(year1, month1, day1, year2, month2, day2):
    """
    Return True if year1-month1-day1 is before year2-month2-day2.
    Otherwise return False
    """
    # * Another practical solution ↴
    # return (year1 != year2) or (month1 != month2) or (day1 != day2)

    if year1 < year2:
        return True
    if year1 == year2:
        if month1 < month2:
            return True
        if month1 == month2:
            return day1 < day2
    return False


def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    assert not dateIsBefore(year2, month2, day2, year1, month1, day1)
    days = 0
    while dateIsBefore(year1, month1, day1, year2, month2, day2):
        days += 1
        year1, month1, day1 = nextDay(year1, month1, day1)
    return days


def test():
    test_cases = [((2012, 1, 1, 2012, 2, 28), 58),
                  ((2012, 1, 1, 2012, 3, 1), 60),
                  ((2011, 6, 30, 2012, 6, 30), 366),
                  ((2011, 1, 1, 2012, 8, 8), 585),
                  ((1900, 1, 1, 1999, 12, 31), 36523)]

    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        if result != answer:
            print("Test with data:", args, "failed", result)
        else:
            print("Test case passed!")


test()
