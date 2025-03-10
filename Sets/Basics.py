   #   1

s1=set([1,2,3,4])
s2={1,2,3,7,8}
print(s1,s2)


#   2

s2={1,2,3,7,8}
print(type(s1),type(s2))

s3={1,2,3,4,8,8,8}
print(s3)

s3.add(5)
print(s3)

print()

s3.update([1,2,2,3,4,5,6,7,7])
print(s3)

print()
s3.remove(8)
print(s3)

print()

s3.discard(1)
print(s3)

poppedelement=s3.pop()
print(s3,poppedelement)
s3.clear()
print(s3)