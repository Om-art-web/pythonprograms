# Loops

n = 10

r = range(n)

for i in range(1, n+1):                # 1st
    print(i, end=",")
print()

for i in range(2, n, 2):                # 2nd
    print(i, end=",")
print()


for i in range(1, n, 2):                # 3rd
    print(i, end=",")
print()

for i in range(1, n+1, 1):              # 4rth
    print(i*i, end=",")

print()
for i in range(1, n):
    print(i*(i+1), end=",")             #5th
print()

for i in range(2, n+1):                #5th
    print(i*(i-1), end=",")
print()



for i in range(1,n+1):                #6th
    print("1/",i,end=",\t")

