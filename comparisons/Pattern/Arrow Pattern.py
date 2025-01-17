n=7
mid=(n+1)//2
for row in range(1,n+1):
    for col in range(1,n+1):
        condition=row==mid or col-row==3 or row+col==11
        if condition:
            print("*",end="")
        else: 
            print(" ",end="")

    print()

