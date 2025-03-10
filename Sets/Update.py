a = {1, 2}
b = {2, 3}
c = {3, 4}


d=a.copy()
d.intersection_update(b)
print("Intersection update ",d)

print('................................')

d=a.copy()
d.difference_update(b)
print("Difference update ",d)

print('................................')

d=a.copy()
d.symmetric_difference_update(b)
print("Symmetric difference update ",d)

