a, b = 7, 8

max = a if a >= b else b
print(max)
print(a if a >= b else b)
c = 7
max = (a if a >= c else c) if a >= b else (b if b >= c else c)
print(max)

