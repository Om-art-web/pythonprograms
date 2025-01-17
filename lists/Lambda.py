a = ["animal", "layer", "train", "ship"]

a.sort(key=lambda x: x[len(x) - 1], reverse=True)

print(a)


print('..................................................')

# a b  RETURN - IF A<B  0 if a==b, +ve if a>b
b=[0,9,-9,87,879,56,435]
import functools as ft
def mycompare(a, b):
    if a%2==0:
        return-1
    return 1
b.sort(key=ft.cmp_to_key(mycompare))
print(b)


print('..................................................')
a= [1,2,3,4,5]
a.sort(key=ft.cmp_to_key(mycompare))
print(a)


print('......................................')


a = [1, 2, 3, 4, 5]
a.sort(key=ft.cmp_to_key(lambda a, b: a - b))
print(a)


print('.......................................')


from numpy import random

a = list(random.randint(100, size=10))
a.sort(key=ft.cmp_to_key(lambda a, b: a - b))
print(a)

print('........................................')
a = [random.randint(100) for x in range(10)]
a.sort(key=ft.cmp_to_key(lambda a, b: a - b))
print(a)
