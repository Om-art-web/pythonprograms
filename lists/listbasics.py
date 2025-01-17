
l=[]                                                   #1st
print(l)
print(type(l))


l=[1,2,3]                                             #2nd
print(l)
l=list([1,2,3])
print(l)

print('.......................')

l=list([1,2,3])                                         #3rd
print('Length is:  ',len(l)) 

print('.......................')

l=list([1,2,3])                                         #4rth
print("0:",l[0],"1:",l[1],"2:",l[2])

print('.......................')

l=list([1,2,3])                                         #5th
print("-1:",l[-1],"-2:",l[-2],"-3",l[-3])


print('.......................')-

l=list([1,2,3])
n=len(l)


for i in range(n):
    print(i,"=",l[i])

print('.................................')



l = [1, "Two", 3, "Four"]
print(l)



for x in l:
    print(x)


print(".....................")


n=len(l)
print(l)

print(".....................")



l=[0,"One",2,"Three",4,"Five"]
print("1 to 3",l[1:4])
print("......................")
print("1 to end",l[1:])
print("......................")
print("Beginning to 3",l[:4])
print("......................")
print("Complete Array ",l[:])
print("......................")
print("Last 1 Elements",l[-1:])
print("......................")
print("2 from last to 4 from last",l[-4:-1])
print("......................")
print("2 from last to 4 from last",l[-4:-2 + 1])

print("......................")
l=[0,1,2,3,4,5,]
print('Min',min(l))
print('Max',max(l))


