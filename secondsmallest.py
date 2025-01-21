# 5  10  sabse chota 3 = 3 5,  beech mein,  6  5,6 , 12   

a=[3,10,4,7,6,7,8]

print(a)  
if a[0]<a[1]:# 1<-4
    min1,min2=a[0],a[1] 
    print("if")
else:  # -1
    min2,min1=a[0],a[1]
    print("else")
n=len(a)
print(min1,min2)
for i in range(2,n):
    value=a[i]
    if value<=min1 :
        min2=min1
        min1=value
        print(min1,min2)
        continue
    if value>min2:
        continue
    min2=value
print(min1,min2)



 

