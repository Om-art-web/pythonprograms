n=10

for row in range(1,n+1):
    for col in range(1,n+1):
        condition= row>col or col>row
        if condition:
            print("*",end="")
        else:
            print(" ",end="")
    print()