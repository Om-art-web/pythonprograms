c, b = 34, 21
print(c, end=",")
print(b, end=",")
a = c-b
while a > 0:
    print(a, end=",")

    c = b
    b = a
    a = c-b
print(a, end=".")
