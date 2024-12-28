a,b=0 ,1
print(a,end=",")
print(b,end=",")
n=10
r=range(n)
for i in range(3,n+1):

    c= a+b
    a=b
    b=c
    print(c,end=",")



a,b = 2,5

print(a)
print(b)