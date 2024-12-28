
# Find the max of three number


a = int(input('First number:  '))
b = int(input('Second number:  '))
c = int(input('Third number:  '))

if a > b and a > c:
    max = a
elif b > c:
    max = b
else:
    max = c
print(max,'maximum number')