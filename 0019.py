year = 1900
day = 1 # 1=Monday ... 7=Sunday
date = 1 # 1-28/29/30/31
month = 1 # 1=January ... 12=December
months_30 = [9, 4, 6, 11]
sunday_count = 0

while year <= 2000:
    # update day
    if day == 7:
        day = 1
    else:
        day += 1

    # update date
    date += 1

    # update month
    if month == 2:
        if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
            if date > 29 :
                month += 1
                date = 1
        else:
            if date > 28:
                month += 1
                date = 1
    elif month in months_30:
        if date > 30:
            month += 1
            date = 1
    else:
        if date > 31:
            month += 1
            date = 1
    if month == 13:
        month = 1

    #  update year
    if month == 12 and date == 31 :
        year += 1

    # count sundays
    if date == 1 and day == 7 and year >= 1901:
        sunday_count += 1

print(sunday_count)
