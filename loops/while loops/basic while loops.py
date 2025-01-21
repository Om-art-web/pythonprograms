

#1,2,3,4

n = 10
i = 1

while i <= n:
    print(i, end=",")                       #1st
    # i += 1
    i -= -1
print()


i = n                                       #Reverse
while i >= 1:
    print(i, end=",")
    # i -= 1
    # i=i-1
    i += -1
print()


i = 2                                 # Even
print("\nEven numbers", end=": ")
while i <= n:
    print(i, end=",")
    i += 2
print()

i=1                                  # Odd
print("\nOdd numbers", end=": ")
while i<=n:
    print(i,end=",")
    i+=2
print()


i = 1                                  # Second even               
n = n//2
print("\nEven numbers", end=": ")
while i <= n-1:
    print(2*i, end=",")
    i += 1
print(2*n, end=".")

print()

             # Third even
n = 10
i = 2
while i <= n:
    if i < n:
        print(i, end=",")
    else:
        print(i, end=".")

    i += 2
print()

                     # 4rth

i=1  
while i<=n:
    print(i*i,end=",")
    i+=1
print()

                      #5th
i=1
while i<=n-1:
    print(i*(i+1),end=",")
    i+=1
       
print()

                     #6th

i=1
while i<=n-1:
    print("1/",i,end=",")
    i+=1
print()

