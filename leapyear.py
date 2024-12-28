    # Leap year


year= int(input('Enter the year:  '))

if year%400==0:
    print(year , "is a leap year")
elif year%4==0 and year%100!=0:
      print(year, 'is a leap year')
else:
     print(year,'year is not a leap year')

'''
year        divby 400           div by 4            div by 100      result

2024        No                     yes                     no       leap year

2000        yes                     yes                 yes         leap year

2025        no                      no                  no          mot leap year

1900        no                      yes                 yes         not leap year
'''