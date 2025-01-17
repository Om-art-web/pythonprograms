
n = 7
for row in range(1, n+1):
    for col in range(1, n+1):
        condition = row == col or col == 1 or col == 7
        if condition:
            print("*", end="")
        else:
            print(" ", end="")
    print()


# n = 7

# for row in range(1, n+1):
#     for col in range(1, n+1):
#         condition = (row-col>=-3) and (row+col>=5) and (row-col<=3) and (row-col<=3)
#         if condition:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()

