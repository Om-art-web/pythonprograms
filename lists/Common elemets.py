a = [5,5,5,5,5]
b = [4,8,9,7,6,5]
common = []
smaller = []
larger = []

n1 = len(a)
n2 = len(b)
if n1 < n2:

    smaller = a
    larger = b
else:
    smaller = b
    larger = a
for x in smaller:
    if x in common:
        continue
    if x in larger:
        common.append(x)

print(common)

print('...........................................')

