monthno= int(input('enter the month:  '))
# print(monthno)
# monthno=1
# print(monthno)
if monthno in (1,3,5,7,8,10,12):
    days=31

elif monthno in (4,6,9,11):
    days=30

elif monthno ==2:
    year=int(input('enter the year'))
    if year%400==0:
        days=29
    elif year%4==0 and year%100!=0:
        days=29
    else:  days=28
else:
    days='invalid'
print(days)



