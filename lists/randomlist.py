from numpy import random
import functools as ft

# a = list(random.randint(100, size=10))
# for i in a:
#     print(i,end=",")

a = [(random.randint(6) +1) for x in range(5)]
print(a)
a.sort(key=ft.cmp_to_key(lambda a, b: a - b))
print(a)



