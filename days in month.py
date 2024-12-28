month = int(input('Enter the month: '))

# month=7
if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
    days = 31
elif month == 4 or month == 6 or month == 9 or month == 11:
    days = 30
elif month == 2:
    year = int(input('Enter the year'))
    # year=2024
    if year % 400 == 0:
        days = 29
    elif year % 4 == 0 and year % 100 != 0:
        days = 29
    else:
        days = 28
else:
    days = "Invalid monthno "
print(days)
