n = 4

for row in range(n, 1, -1):
    for space in range(1, n-row+1):
        print(" ", end="")
    for star in range(1, 2*row, +1):
        print("0", end="")
    print()


for row in range(1, n+1):
    for space in range(1, n-row+1):
        print(" ", end="")
    for star in range(1, 2*row, +1):
        print("0", end="")
    print()


print()
print()
