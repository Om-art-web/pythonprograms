a,b=0,1

print(a,end=",")
print(b,end=",")

n=10

i=3

while i <=n:

    c=a+b
    a=b
    b=c
    i+=1
    print(c,end=",")

    