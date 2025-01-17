n = 5
# for i in range(256):
#     print(i, chr(i), end=",")
# print(ord('A'))
# print(chr(65))
for row in range(1, n+1):
    for star in range(1, row+1):
        print(star, end="")
    print()

base = ord("a")-1
for row in range(1, n+1):
    for star in range(1, row+1):
        ch = chr(base + star)
        print(ch, end="")
    print()
