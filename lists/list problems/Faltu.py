a=[1,2,3,4,5]
print(a)
# a[0],a[-1]=a[-1],a[0]
# # print(a)


# a[1],a[-2]=a[-2],a[1]
# # print(a)

n=len(a)
mid=n//2
# print(n,mid)
for i in range(mid):
    # print(i,-i-1)

    a[i],a[-i-1]=a[-i-1],a[i]
    a[i]=a[-i-1]
    a[i]=a[-i-1]
print(a)
