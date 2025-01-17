n = 5
horizontal = 2*n+1
for row in range(1, n):
    for left in range(1, row+1):
        print("*", end="")
    mid = horizontal-2*row
    for space in range(1, mid):
        print(" ", end="")

    for right in range(1, row+1):
        print("*", end="")

    print()
for i in range(1, horizontal):
    print("*", end="")
print()


