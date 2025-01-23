# print("..............AND...................")
# print(True and True)
# print(True and False)
# print(False and True)
# print(False and False)
# print("..............OR...................")
# print(True or True)    
# print(True or False)
# print(False or True)
# print(False or False)


list1=[1,-3,2,56,-45,3,-67]

positive,negative=[],[]

n=len(list1)
print(n)

for i in range(0,n):
    if list1[i]>0:
        positive.append(list1[i])
    else:
        negative.append(list1[i])
print(positive,negative)