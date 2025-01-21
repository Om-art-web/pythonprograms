#  90 to 100 = A grade   80 to 90 = B   If Exact 90  then the B grade

#  80 to 50 = C Grade    50 to 30 = D Grade

marks= int(input('Enter the marks = '))

if marks<=100:
    print('A Grade')
elif marks<90:
    print("B Grade")
elif marks==90:
    print('B Grade')
elif marks<80:
    print("C Grade")
else:
    print("D Grade")
    