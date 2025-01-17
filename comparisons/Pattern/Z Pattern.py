n=7

for row in range(1,n+1):
    for col in range(1,n+1):
        condition= row==1 or row+col==8 or row==7
        if condition:
            print("*",end="")
        else:
            print(" ",end="")
    print()

