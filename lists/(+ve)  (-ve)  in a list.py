# a = [1,45,-56,-34,-21,23]

# positive,negative =[],[]

# n=len(a)
# for i in range(0,n):
#     if a[i]>=0:
#         positive.append(a[i])
#     else:        negative.append(a[i])
# print(positive,negative)


b=[1,2,3,5,4,-2,-4,5,-9]


positive,negative=[],[]


n=len(b)
print(n)

for i in range(0,n):
    if b[i]>=0:
        positive.append(b[i])
    else:
        negative.append(b[i])
print(positive,negative)



