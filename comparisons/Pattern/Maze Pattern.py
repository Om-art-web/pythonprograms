
                         #1st


n=7

for row  in range(1,n+1):                                                   
    for col in range(1,n+1):
        condition= row +col==5 or row-col==3 or col-row==3 or row+col==11
        if condition:
            print(" ",end="")
        else:
            print("*",end="")
    print()

print()
print()


                                  #2nd

n=7

for row in range(1,n+1):
    for col in range(1,n+1):
        condition=row+col==5 or row-col==3 or col-row==3 or row+col==11
        if  condition:
            print("*",end="")
        else:
            print(" ",end="")
    print()



