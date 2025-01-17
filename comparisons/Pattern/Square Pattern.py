n=5

for row in range(1,n+1):
    for col in range(1,n+1):
        condition=col==1 or row==1 or col==n or row==n
        if condition:
            print("*",end="")
        else:
            print(" ",end="")
    print()