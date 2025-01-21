a = [2, 4, 6, 3, 5]
b = [1, 9, 6, 3, 7]

common = []

for x in a:
    if x in common:
        continue
    if x not in b :
        common.append(x)
print(common)

for x in b:
    if x in common:
        continue
    if x not in a:
        common.append(x)
print(common)


