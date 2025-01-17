n=5

for row in range(1,n+1):
    for star in range(1,row+1):
        print(row+1-star,end="")
    print()

'''
A   B   C           X      Y    Z
1   2   3           24     25   26
26  25  24
1,2,3
3,2,1
'''