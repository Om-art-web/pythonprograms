a, b, c = 9, 7, 8
'''
a       b       c 
2       3       1  a<=b and a>=c
2       1       3  a>=b and a <=c

1       2       3
3       2       1

'''

if a<=b and a>=c or a>=b and a<=c:
    mid=a
elif b<=a and b>=c or b<=c and b>=a:
    mid=b
else:
    mid=c
print(mid)
