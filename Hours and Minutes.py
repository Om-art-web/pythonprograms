# Hours and minutes


hour = int(input('Enter the hour:  '))
minute = int(input('Enter the minutes:  '))

if hour > 12:
    print("Minus PM")
    print(hour-12, ":", minute, "PM")
elif hour == 12:
    print("Bina minus wala PM")
    print(hour, ":", minute, "PM")

else:

    print(hour, ":",minute, "AM")








    
