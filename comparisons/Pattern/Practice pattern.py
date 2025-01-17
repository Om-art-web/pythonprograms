# # n=5

# # for row in range(1,n+1):
# #     for star in range(1,row+1):
# #         print("*",end="")
# #     print()



# #other pattern

# n=5
# for i in range(n,0,-1):
#     for star in range(1,i+1):
#         print("*",end="")
#     print()

# n=7

# for i in range(n,0,-1):
#     for star in range(1,i+1):
#         print("*",end="")
#     print()



# n=8

# for row in range(1,n+1):
#     for space in range(1,n-row+1):
#         print(" ",end="")
#     for star in range(1,row+1):
#         print("*",end="")
#     print()

# n=5

# for row in range(1,n+1):
#     for space in range(1,n-row+1):
#         print("<!>",end="")
#     print()
n=5


for row in range(1,n+1):
    for star in range(1,row+1):
        print("*",end="")
    print()

for row in range(n,1,+1):
    for star in range(1,row+1):
        print("*",end="")
    print()