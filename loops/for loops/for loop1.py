# r=range(start=0,stop,step=1)stop is set to stop-1
n = 10
r = range(n)
for i in r:
    print(i, end=",")
print()
for i in range(1, n):
    print(i, end=",")
print()
for i in range(1, n+1):
    print(i, end=",")
print()
for i in range(1, n, 2):
    print(i, end=",")
print()
for i in range(2, n, 2):
    print(i, end=",")
print()

# for i in range(n, 0, -1):
#     print(i, end=",")
# print()

for i in reversed(range(1, n+1)):
    print(i, end=",")
print() 
